import re

from flake8_digit_separator.classifiers.base import NumberValidator


# class ComplexClassifier(NumberValidator):
#     def __init__(self, token):
#         self._token = token

#     @property
#     def token(self):
#         return self._token

#     @property
#     def type_name(self):
#         return 'complex'

#     @property
#     def re_expression(self):
#         return (
#             r'^[+-]?('
#             r'('
#             r'\d[\d_]*(\.\d[\d_]*)?([eE][+-]?\d[\d_]*)?|'    # Decimal numbers
#             r'\.\d[\d_]*([eE][+-]?\d[\d_]*)?|'               # Numbers starting with a point
#             r'0[xX][\da-fA-F_]+(\.[\da-fA-F_]*)?|'           # HEX with decimal point
#             r'0[bB][01_]+|'                                  # Binary numbers
#             r'0[oO][0-7_]+'                                  # Octal numbers
#             r')'
#             r')[jJ]$'
#         )

#     def check(self) -> bool:
#         return bool(re.fullmatch(
#             self.re_expression,
#             self.token,
#             flags=re.IGNORECASE,
#         ))

#     def validate(self):
#         ...

#     @property
#     def error_message(self):
#         ...


class HexClassifier(NumberValidator):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'hex'

    @property
    def re_expression(self):
        return r'^[+-]?0[xX][\da-fA-F_]+$'

    def check(self) -> bool:
        return bool(re.fullmatch(self.re_expression, self.token))

    def validate(self):
        token = self.token.lstrip('+-').lower()
        cleaned = token.replace('_', '')
        
        if not token.startswith('0x_'):
            return False
        elif len(cleaned) >= 5:
            if '_' in token:
                if not re.fullmatch(r'^[0-9a-f]{1,4}(?:_[0-9a-f]{4})+$', token[3:]):
                    return False
            else:
                return False
        elif len(cleaned) < 5 and '_' in cleaned:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS400: HEX'


class BinaryClassifier(NumberValidator):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'binary'

    @property
    def re_expression(self):
        return r'^[+-]?0[bB][01_]+$'

    def check(self) -> bool:
        return bool(re.fullmatch(self.re_expression, self.token))

    def validate(self):
        token = self.token.lstrip('+-').lower()
        cleaned = token.replace('_', '')

        if not token.startswith('0b_'):
            return False
        elif len(cleaned) >= 5:
            if '_' in token:
                if not re.fullmatch(r'^\d{1,4}(?:_\d{4})+$', token[3:]):
                    return False
            else:
                return False
        elif len(cleaned) < 5 and '_' in cleaned:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS300: BINARY'


class OctalClassifier(NumberValidator):
    def __init__(self, token: str):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'octal'

    @property
    def re_expression(self):
        ...

    def check(self) -> bool:
        token: str = self.token.lower().lstrip('+-').replace('_', '')
        token_without_prefix: str = token[2:]
        octal_digits: set[str] = set(str(digit) for digit in range(8))

        try:
            int(token, 8)
        except ValueError:
            return False

        return bool(
            token.startswith('0o')
            and all(digit in octal_digits for digit in token_without_prefix)
        )

    def validate(self):
        token = self.token.lstrip('+-').lower()
        cleaned = token.replace('_', '')

        if not token.startswith('0o_'):
            return False
        elif len(cleaned) >= 4:
            if '_' in token:
                if not re.fullmatch(r'^\d{1,3}(?:_\d{3})+$', token[3:]):
                    return False
            else:
                return False
        elif len(cleaned) < 4 and '_' in cleaned:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS200: OCT'


# class ScientificClassifier(NumberValidator):
#     def __init__(self, token):
#         self._token = token

#     @property
#     def token(self):
#         return self._token.lower()

#     @property
#     def type_name(self):
#         return 'scientific'

#     def check(self) -> bool:
#         return 'e' in self.token

#     def validate(self):
#         ...

#     @property
#     def error_message(self):
#         ...


class DecimalClassifier(NumberValidator):
    def __init__(self, token: str):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'decimal'

    def check(self) -> bool:
        if '.' in self.token:
            sep = self.token.split('.')
            if len(sep) == 2:
                left, right = sep[0], sep[1]
                try:
                    if left != '':
                        int(left, 10)
                        int(right, 10)
                        return True
                    else:
                        int(right, 10)
                        return True
                except ValueError:
                    return False
                
        return False

    def validate(self):
        token = self.token.lstrip('+-')

        parts = token.split('.')

        for part in parts:
            cleaned = part.replace('_', '')
            if len(cleaned) >= 4:
                if '_' in token:
                    if not re.fullmatch(r'^\d{1,3}(?:_\d{3})+$', part):
                        return False
                else:
                    return False
            elif len(cleaned) < 4 and '_' in part:
                return False

        return True

    @property
    def error_message(self):
        return 'FDS400: DECIMAL/FLOAT'


class IntClassifier(NumberValidator):
    def __init__(self, token):
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def type_name(self):
        return 'int'

    @property
    def re_expression(self):
        return r'^[+-]?\d[\d_]*$'

    def check(self) -> bool:
        return bool(re.fullmatch(self.re_expression, self.token))

    def validate(self) -> bool:
        """
        Wrong: 100000, 10000_0, 1_0000, 10_00000
        Correct: 1_000, 10_000, 100_000, 10, 100, 10_000_000

        :return: _description_
        :rtype: bool
        """
        token = self.token.lstrip('+-')
        cleaned = token.replace('_', '')

        if len(cleaned) >= 4:
            if '_' in token:
                if not re.fullmatch(r'^\d{1,3}(?:_\d{3})+$', token):
                    return False
            else:
                return False
        elif len(cleaned) < 4 and '_' in token:
            return False

        return True

    @property
    def error_message(self):
        return 'FDS100: INT'


a = 100

b = 0o_360_363

с = 0b_0_0111_1110_1001_1100

d = 0x_CAFE_F00D

e = 12_123.1_231_231