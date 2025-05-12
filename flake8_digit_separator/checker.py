import ast
import tokenize

from flake8_digit_separator import version
from flake8_digit_separator.classifiers.factory import ClassifiersFactory


class Classifier:
    def __init__(self, token):
        self._token = token
        self._classifiers = ClassifiersFactory(self._token).create_ordered_classifiers()

    @property
    def classifiers(self):
        return self._classifiers

    @property
    def token(self):
        self._token

    def classify(self):
        for classifier in self.classifiers:
            if classifier.check():
                return classifier


class Checker:
    name = version.NAME
    version = version.VERSION

    def __init__(self, tree: ast.AST, file_tokens):
        self.file_tokens = file_tokens

    def run(self):
        for token in self.file_tokens:
            if token.type == tokenize.NUMBER:
                # (line, column, msg, type)
                yield token.start[0], token.start[1], f'FDS100 TOKEN: {token.string}', type(self)
