#!/bin/bash

own_dir="$( cd "$(dirname "${BASH_SOURCE[0]}")" || exit && pwd -P )" # this gives the full path, even for sourced scripts

# shellcheck disable=SC1090
source "${own_dir}/lib_bash_functions.sh"
# install_dependencies

project_root_dir="${project_root_dir}"

# run_pytest --log_cli_level="WARNING"
run_pytest --disable-warnings --log-cli-level=ERROR
