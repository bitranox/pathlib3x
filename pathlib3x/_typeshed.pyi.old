# taken from https://raw.githubusercontent.com/python/typeshed/master/stdlib/2and3/_typeshed/__init__.pyi
# to get PathLike, StrPath, OpenBinaryMode, OpenTextMode

import sys
from typing import Union
# https://github.com/python/typeshed/blob/master/third_party/2and3/typing_extensions.pyi
from typing_extensions import Literal

from typing import Text
if sys.version_info >= (3, 6):
    from os import PathLike

    StrPath = Union[str, PathLike[str]]
    BytesPath = Union[bytes, PathLike[bytes]]
    AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
else:
    StrPath = Text
    BytesPath = bytes
    AnyPath = Union[Text, bytes]

OpenTextMode = Literal[
    "r",
    "r+",
    "+r",
    "rt",
    "tr",
    "rt+",
    "r+t",
    "+rt",
    "tr+",
    "t+r",
    "+tr",
    "w",
    "w+",
    "+w",
    "wt",
    "tw",
    "wt+",
    "w+t",
    "+wt",
    "tw+",
    "t+w",
    "+tw",
    "a",
    "a+",
    "+a",
    "at",
    "ta",
    "at+",
    "a+t",
    "+at",
    "ta+",
    "t+a",
    "+ta",
    "x",
    "x+",
    "+x",
    "xt",
    "tx",
    "xt+",
    "x+t",
    "+xt",
    "tx+",
    "t+x",
    "+tx",
    "U",
    "rU",
    "Ur",
    "rtU",
    "rUt",
    "Urt",
    "trU",
    "tUr",
    "Utr",
]

OpenBinaryModeUpdating = Literal[
    "rb+",
    "r+b",
    "+rb",
    "br+",
    "b+r",
    "+br",
    "wb+",
    "w+b",
    "+wb",
    "bw+",
    "b+w",
    "+bw",
    "ab+",
    "a+b",
    "+ab",
    "ba+",
    "b+a",
    "+ba",
    "xb+",
    "x+b",
    "+xb",
    "bx+",
    "b+x",
    "+bx",
]
OpenBinaryModeWriting = Literal[
    "wb", "bw", "ab", "ba", "xb", "bx",
]
OpenBinaryModeReading = Literal[
    "rb", "br", "rbU", "rUb", "Urb", "brU", "bUr", "Ubr",
]
OpenBinaryMode = Union[OpenBinaryModeUpdating, OpenBinaryModeReading, OpenBinaryModeWriting]
