#!/bin/bash
save_dir="$PWD"
own_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit && pwd -P)" # this gives the full path, even for sourced scripts

sleeptime_on_error=5
sudo_askpass="$(command -v ssh-askpass)"
export SUDO_ASKPASS="${sudo_askpass}"
export NO_AT_BRIDGE=1 # get rid of (ssh-askpass:25930): dbind-WARNING **: 18:46:12.019: Couldn't register with accessibility bus: Did not receive a reply.

tests_dir="${own_dir}"
project_root_dir="$(dirname "${tests_dir}")"              # one level up
export PYTHONPATH="${project_root_dir}:/media/srv-main-softdev/rotek-apps/lib:${PYTHONPATH}"

function install_or_update_lib_bash() {
  if [[ ! -f /usr/local/lib_bash/install_or_update.sh ]]; then
    sudo git clone https://github.com/bitranox/lib_bash.git /usr/local/lib_bash 2>/dev/null
    sudo chmod -R 0755 /usr/local/lib_bash 2>/dev/null
    sudo chmod -R +x /usr/local/lib_bash/*.sh 2>/dev/null
    sudo /usr/local/lib_bash/install_or_update.sh 2>/dev/null
  else
    /usr/local/lib_bash/install_or_update.sh
  fi
}

install_or_update_lib_bash

source /usr/local/lib_bash/lib_helpers.sh

function my_banner() {
  banner "${project_root_dir}: ${1}"
}

function my_banner_warning() {
  banner_warning "${project_root_dir}: ${1}"
}

function clean_caches() {
  # mypy and pytest caches should be deleted, because sometimes problems on collecting if not
  clr_green "clean caches and distribution directories in ${project_root_dir}"
  sudo find "${project_root_dir}" -name ".eggs" -type d -exec rm -rf {} \; 2>/dev/null
  sudo find "${project_root_dir}" -name ".mypy_cache" -type d -exec rm -rf {} \; 2>/dev/null
  sudo find "${project_root_dir}" -name ".pytest_cache" -type d -exec rm -rf {} \; 2>/dev/null
  sudo find "${project_root_dir}" -name "build" -type d -exec rm -rf {} \; 2>/dev/null
  sudo find "${project_root_dir}" -name "dist" -type d -exec rm -rf {} \; 2>/dev/null
  sudo find "${project_root_dir}" -name "*.egg-info" -type d -exec rm -rf {} \; 2>/dev/null
  sudo rm -rf "$HOME/.eggs/*"
  sudo rm -rf "$HOME/.mypy_cache"
}

function install_virtualenv_debian() {
  clr_green "installing virtualenv"
  sudo apt-get install python3-virtualenv
}

function install_test_requirements() {
  # this should be already installed, but it happens that pycharm ide venv does not have it
  clr_green "install_requirements"
  sudo chmod -R 0777 ~/.eggs # make already installed eggs accessible, just in case they were installed as root

  python3 -m pip install --upgrade pip
  python3 -m pip install --upgrade setuptools
  python3 -m pip install --upgrade wheel

  # we dont istall project requirements - that should be ONLY installed in the venv !
  # if test -f "${project_root_dir}/requirements.txt"; then
  #   python3 -m pip install --upgrade -r "${project_root_dir}/requirements.txt"
  # else
  #   clr_red "requirements.txt not found"
  # fi

  if test -f "${project_root_dir}/requirements_test.txt"; then
    python3 -m pip install --upgrade -r "${project_root_dir}/requirements_test.txt"
  else
    clr_red "requirements_test.txt not found"
  fi
}

function install_dependencies() {
  clr_green "installing dependencies"
  install_virtualenv_debian
  install_test_requirements
}

function delete_virtual_environment() {
  sudo rm -rf ~/venv
}

function install_clean_virtual_environment() {
  clr_green "installing venv"
  delete_virtual_environment
  virtualenv ~/venv
}

function cleanup() {
  trap '' 2   # disable Ctrl+C
  delete_virtual_environment
  clean_caches
  cd "${save_dir}" || exit
  trap 2      # enable Ctrl+C
}

function pytest_codestyle_mypy() {
  my_banner "pytest --pycodestyle --mypy"
  if ! python3 -m pytest "${project_root_dir}" --disable-warnings; then
    my_banner_warning "pytest --pycodestyle --mypy ERROR"
    beep
    sleep "${sleeptime_on_error}"
    return 1
  fi
}

function mypy_strict() {
  my_banner "mypy strict"
  if ! python3 -m mypy "${project_root_dir}" --strict --warn-unused-ignores --implicit-reexport --follow-imports=silent; then
    my_banner_warning "mypy strict ERROR"
    beep
    sleep "${sleeptime_on_error}"
    return 1
  fi
}

function mypy_strict_with_imports() {
  my_banner "mypy strict including imports"
  if ! python3 -m mypy "${project_root_dir}" --strict --warn-unused-ignores --implicit-reexport --follow-imports=normal; then
    my_banner_warning "mypy strict including imports ERROR"
    beep
    sleep "${sleeptime_on_error}"
    return 1
  fi
}

function install_pip_requirements_venv() {
  if test -f "${project_root_dir}/requirements.txt on virtual environment"; then
    my_banner "pip install -r requirements.txt"
    install_clean_virtual_environment
    if ! ~/venv/bin/python3 -m pip install -r "${project_root_dir}/requirements.txt"; then
      my_banner_warning "pip install -r requirements.txt ERROR"
      beep
      sleep "${sleeptime_on_error}"
      return 1
    fi
  fi
}

function setup_install_venv() {
  if test -f "${project_root_dir}/setup.py"; then
    my_banner "setup.py install on virtual environment"
    install_clean_virtual_environment
    cd "${project_root_dir}" || exit
    if ! ~/venv/bin/python3 "${project_root_dir}/setup.py" install; then
      my_banner_warning "setup.py install ERROR"
      beep
      sleep "${sleeptime_on_error}"
      return 1
    fi
  fi
}

function test_commandline_interface_venv() {
  # this will fail if rotek lib directory is in the path - keep this as a reminder
  my_banner "test commandline interface on virtual environment"

  clr_green "issuing command : $HOME/venv/bin/pathlib3x --version"
  if ! "$HOME/venv/bin/pathlib3x" --version; then
    my_banner_warning "test commandline interface on virtual environment ERROR"
    beep
    sleep "${sleeptime_on_error}"
    return 1
  fi
}

function test_setup_test_venv() {
  if test -f "${project_root_dir}/setup.py"; then
    my_banner "setup.py test"
    install_clean_virtual_environment
    cd "${project_root_dir}" || exit
    if ! ~/venv/bin/python3 "${project_root_dir}/setup.py" test; then
      my_banner_warning "setup.py test ERROR"
      beep
      sleep "${sleeptime_on_error}"
      return 1
    fi
  fi
}

# cleanup on cntrl-c
trap cleanup EXIT
