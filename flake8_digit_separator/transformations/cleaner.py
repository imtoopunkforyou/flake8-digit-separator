import re
from typing import ClassVar, TypeVar, final

SelfCleaner = TypeVar('SelfCleaner', bound='Cleaner')


@final
class Cleaner:
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'[+\-_]')

    def __init__(self: SelfCleaner, text: str) -> None:
        self._text = text

    @property
    def text(self: SelfCleaner) -> str:
        return self._text

    def clean(self: SelfCleaner) -> str:
        return self.pattern.sub('', self._text)
