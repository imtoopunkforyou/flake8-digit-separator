import re
from typing import ClassVar, TypeVar, final

SelfCleaner = TypeVar('SelfCleaner', bound='Cleaner')


@final
class Cleaner:
    """Clears the text by `pattern` argument."""

    pattern: ClassVar[re.Pattern[str]] = re.compile(r'[+\-_]')
    """`+`, `-` and `_` symbols."""

    def __init__(self: SelfCleaner, text: str) -> None:
        self._text = text

    @property
    def text(self: SelfCleaner) -> str:
        """Uncleaned text."""
        return self._text

    def clean(self: SelfCleaner) -> str:
        """Cleaned text."""
        return self.pattern.sub('', self._text)
