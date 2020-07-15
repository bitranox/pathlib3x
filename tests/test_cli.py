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
    result = subprocess.run(command, shell=True, capture_output=True)
    if result.returncode == 0:
        return True
    else:
        if log:
            # You need to enable --log-cli-level=CRITICAL to see that output in pytest
            logger.critical('\n'.join(['STDOUT for {}:'.format(command), result.stdout.decode()]))
            logger.critical('\n'.join(['STDOUT for {}:'.format(command), result.stderr.decode()]))
        return False


def test_cli_commands():
    assert not call_cli_command('--unknown_option', log=False)
    assert call_cli_command('--version')
    assert call_cli_command('-h')
    assert call_cli_command('info')
