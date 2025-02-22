from __future__ import annotations

import sys

TYPE_CHECKING = False

if sys.version_info >= (3, 11):  # YORE: EOL 3.10: 🔪
    BaseExceptionGroup: TypeAlias = BaseExceptionGroup  # noqa: PLW0127, F821
    ExceptionGroup: TypeAlias = ExceptionGroup  # noqa: PLW0127, F821
else:
    from exceptiongroup import BaseExceptionGroup, ExceptionGroup

if TYPE_CHECKING:
    if sys.version_info >= (3, 10):  # YORE: EOL 3.9: 🔪
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

if TYPE_CHECKING:
    if sys.version_info >= (3, 13):  # YORE: EOL 3.12: 🔪
        from typing import TypeVar
    else:
        from typing_extensions import TypeVar

__all__ = (
    "BaseExceptionGroup",
    "ExceptionGroup",
    "TypeAlias",
    "TypeVar",
)
