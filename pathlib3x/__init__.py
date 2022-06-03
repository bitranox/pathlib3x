__all__ = ["PurePath", "PurePosixPath", "PureWindowsPath", "Path", "PosixPath", "WindowsPath"]
import sys
if sys.version_info < (3, 10):
    import pathlib as pathlib_original
from .pathlib3x import *

from . import __init__conf__

__title__ = __init__conf__.title
__version__ = __init__conf__.version
__name__ = __init__conf__.name
__url__ = __init__conf__.url
__author__ = __init__conf__.author
__author_email__ = __init__conf__.author_email
