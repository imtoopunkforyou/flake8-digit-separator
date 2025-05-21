import re
from typing import ClassVar, final


@final
class Cleaner:
    pattern: ClassVar[re.Pattern] = re.compile(r'[+\-_]')

    def __init__(self, text: str) -> None:
        self._text = text

    @property
    def text(self) -> str:
        return self._text

    def clean(self) -> str:
        return self.pattern.sub('', self._text)
