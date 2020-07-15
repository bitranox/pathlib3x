# STDLIB
import logging
import pathlib
import subprocess
import sys

logger = logging.getLogger()
package_dir = 'pathlib3x'
cli_filename = 'pathlib3x_cli.py'

path_cli_command = pathlib.Path(__file__).resolve().parent.parent / package_dir / cli_filename


def call_cli_command(commandline_args: str = '', log: bool = True) -> bool:
    command = ' '.join([sys.executable, str(path_cli_command), commandline_args])
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as exc:
        return False
    return True


def test_cli_commands() -> None:
    # we need the type ignores because of a bug in python 3.8.1 with setup.py test on travis
    assert not call_cli_command('--unknown_option')     # type: ignore
    assert call_cli_command('--version')                # type: ignore
    assert call_cli_command('-h')                       # type: ignore
    assert call_cli_command('info')                     # type: ignore
