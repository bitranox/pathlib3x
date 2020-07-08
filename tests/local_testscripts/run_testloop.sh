#!/bin/bash
own_dir="$( cd "$(dirname "${BASH_SOURCE[0]}")" || exit && pwd -P )" # this gives the full path, even for sourced scripts

# shellcheck disable=SC2050
if [[ "True" != "True" ]]; then
    echo "exit - ${BASH_SOURCE[0]} is not configured by PizzaCutter"
    exit 0
fi

# shellcheck disable=SC1090
source "${own_dir}/lib_bash_functions.sh"
project_root_dir="${project_root_dir}"
do_mypy_tests="True"  # this is set py PizzaCutter
# cleanup on cntrl-c
trap cleanup EXIT

# install dependencies
install_dependencies

function pytest_loop {
    while true; do
        banner "Project Root Dir: ${project_root_dir}"
        cleanup
        # pytest options can be passed to run_pytest like --disable-warnings
        # --log-cli-level=ERROR shows error in pytest if we log to logger.ERROR
        # if ! run_pytest --disable-warnings --log-cli-level=ERROR; then continue; fi
        if ! run_pytest --disable-warnings; then continue; fi

        if [ "${do_mypy_tests}" == "True" ]; then
            if ! mypy_strict; then continue; fi
            if ! mypy_strict_with_imports; then continue; fi
        fi

        if ! install_pip_requirements_venv; then continue; fi
        if ! setup_install_venv; then continue; fi
        if ! test_commandline_interface_venv; then continue; fi
        if ! test_setup_test_venv; then continue; fi

        banner "ALL TESTS PASSED for ${project_root_dir}"
        banner "ALL TESTS PASSED for ${project_root_dir}"
        banner "ALL TESTS PASSED for ${project_root_dir}"
        sleep 5
    done

}

# upgrade_pytest
# upgrade_mypy
pytest_loop
