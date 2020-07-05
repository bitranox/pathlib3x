# taken from https://github.com/python/typeshed/blob/master/third_party/2and3/typing_extensions.pyi
# to define Literal

from typing import Any

class _SpecialForm:
    def __getitem__(self, typeargs: Any) -> Any: ...

Literal: _SpecialForm = ...
