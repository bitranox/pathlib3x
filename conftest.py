import platform
from typing import List

collect_ignore = ['setup.py']


def pytest_cmdline_preparse(args: List[str]) -> None:
    """
    # run tests on multiple processes if pytest-xdist plugin is available
    # unfortunately it does not work with codecov
    import sys
    if "xdist" in sys.modules:  # pytest-xdist plugin
        import multiprocessing

        num = int(max(multiprocessing.cpu_count() / 2, 1))
        args[:] = ["-n", str(num)] + args
    """

    additional_mypy_args: List[str] = list()
    additional_pycodestyle_args: List[str] = list()

    # add mypy option if not pypy
    # if platform.python_implementation() != "PyPy" and sys.version_info >= (3, 5) and sys.version_info != (3, 6):  # type: ignore
    if platform.python_implementation() != "PyPy":
        additional_mypy_args = ['--mypy']

    additional_pycodestyle_args = ['--pycodestyle']
    args[:] = list(set(args + additional_mypy_args + additional_pycodestyle_args))
