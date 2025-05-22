import ast
import tokenize

from flake8_digit_separator import __version__ as version
from flake8_digit_separator.classifiers.classifier import Classifier
from flake8_digit_separator.error import Error
from flake8_digit_separator.numbers.base import Number
from flake8_digit_separator.validators.registry import ValidatorRegistry


class Checker:
    name = version.NAME
    version = version.VERSION

    def __init__(self, tree: ast.AST, file_tokens: list[tokenize.TokenInfo]):
        self.file_tokens = file_tokens

    def run(self):
        for token in self.file_tokens:
            if token.type == tokenize.NUMBER:
                error = self._process_number_token(token)
                if error:
                    yield error.as_tuple()

    def _process_number_token(self, token: tokenize.TokenInfo) -> Error | None:
        classifier = Classifier(token.string)
        number: Number = classifier.classify()

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
