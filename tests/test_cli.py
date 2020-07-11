# EXT
from click.testing import CliRunner

# OWN
import pathlib3x.pathlib3x_cli as pathlib3x_cli

runner = CliRunner()
runner.invoke(pathlib3x_cli.cli_main, ['--version'])
runner.invoke(pathlib3x_cli.cli_main, ['-h'])
runner.invoke(pathlib3x_cli.cli_main, ['info'])
