import ast
import tokenize
from typing import Iterator, TypeVar

from flake8_digit_separator import __version__ as version
from flake8_digit_separator.classifiers.registry import ClassifierRegistry
from flake8_digit_separator.error import Error
from flake8_digit_separator.types import ErrorMessage
from flake8_digit_separator.validators.registry import ValidatorRegistry

SelfChecker = TypeVar('SelfChecker', bound='Checker')


class Checker:
    name = version.NAME
    version = version.VERSION

    def __init__(
        self: SelfChecker,
        tree: ast.AST,
        file_tokens: list[tokenize.TokenInfo],
    ) -> None:
        self.file_tokens = file_tokens

    def run(self: SelfChecker) -> Iterator[ErrorMessage]:
        for token in self.file_tokens:
            if token.type == tokenize.NUMBER:
                error = self._process_number_token(token)
                if error:
                    yield error.as_tuple()

    def _process_number_token(
        self: SelfChecker,
        token: tokenize.TokenInfo,
    ) -> Error | None:
        classifiers = ClassifierRegistry.get_ordered_classifiers()
        for classifier in classifiers:
            number = classifier(token.string).classify()
            if number:
                break

        if not number.is_supported:
            return None

        validator = ValidatorRegistry.get_validator(number)
        if validator.validate():
            return None

        return Error(
            line=token.start[0],
            column=token.start[1],
            message=validator.error_message,
            object_type=type(self),
        )
