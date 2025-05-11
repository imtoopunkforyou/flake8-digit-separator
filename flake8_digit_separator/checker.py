import ast
import tokenize

from flake8_digit_separator import version


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