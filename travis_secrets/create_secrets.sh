#!/bin/bash
save_dir="$PWD"
own_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit && pwd -P)" # this gives the full path, even for sourced scripts

# shellcheck disable=SC1090
source "${own_dir}/create_secrets_bash_helpers.sh"

project_root_dir="${project_root_dir}"

install_dependencies

banner "this will encrypt the name and the value of a secret environment variable for travis."

read -r -p 'variable name  :' var_name
read -r -p 'variable value :' var_value

cd "${project_root_dir}"||exit
travis encrypt "${var_name}=${var_value}" --no-interactive > "${own_dir}/secrets/${var_name}.secret.txt"

banner "You need to run PizzaCutter to import that secret into travis.yml"
wait_for_enter
cd "${save_dir}" || exit
