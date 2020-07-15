import sys
import traceback
from typing import TextIO


class _Config(object):
    traceback: bool = False


config = _Config()


def get_system_exit_code(exc: BaseException) -> int:
    """
    Return the exit code for linux or windows, based on the exception.
    If, on windows, the winerror is set on the Exception, we return that winerror code.

    >>> try:
    ...     raise FileNotFoundError()
    ... except FileNotFoundError as exc:
    ...     assert get_system_exit_code(exc) == 2
    ...     setattr(exc, 'winerror', 42)
    ...     assert get_system_exit_code(exc) == 42

    """

    # from https://www.thegeekstuff.com/2010/10/linux-error-codes
    # dict key sorted from most specific to unspecific
    posix_exceptions = {FileNotFoundError: 2, PermissionError: 13, FileExistsError: 17, TypeError: 22,
                        ValueError: 22, RuntimeError: 1, BaseException: 1}
    windows_exceptions = {FileNotFoundError: 2, PermissionError: 5, ValueError: 13, FileExistsError: 80, TypeError: 87,
                          RuntimeError: 1, BaseException: 1}

    if hasattr(exc, 'winerror'):
        try:
            exit_code = int(exc.winerror)    # type: ignore
            return exit_code
        except (AttributeError, TypeError):
            pass

    if 'posix' in sys.builtin_module_names:
        exceptions = posix_exceptions
    else:
        exceptions = windows_exceptions

    for exception in exceptions:
        if isinstance(exc, exception):
            return exceptions[exception]
    return 1


def print_exception_message(trace_back: bool = config.traceback, stream: TextIO = sys.stderr) -> None:
    """
    Prints the Exception Message to stderr

    if trace_back is True, it also prints the traceback information

    >>> try:
    ...     raise FileNotFoundError('test')
    ... except Exception:       # noqa
    ...     print_exception_message(False)
    ...     print_exception_message(True)


    """
    exc_info = sys.exc_info()[1]
    if exc_info is not None:
        exc_info_type = type(exc_info).__name__
        exc_info_msg = ''.join([exc_info_type, ': ', exc_info.args[0]])
        if trace_back:
            exc_info_msg = ''.join(['Traceback Information : \n', traceback.format_exc()]).rstrip('\n')
        print(exc_info_msg, file=stream)
