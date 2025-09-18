from flake8_digit_separator.rules.base import FDSRules
from flake8_digit_separator.rules.rules import (
    BinaryFDSRules,
    FloatFDSRules,
    HexFDSRules,
    IntFDSRules,
    OctalFDSRules,
)


class TestFDSRules:
    """Test FDSRules enum."""

    def test_init_sets_text_and_example(self):
        """Test that __init__ sets text and example correctly."""

        class TestRule(FDSRules):
            TEST_RULE = 'Test rule text', 'test_example'

        rule = TestRule.TEST_RULE

        assert rule.text == 'Test rule text'
        assert rule.example == 'test_example'

    def test_create_message_formats_correctly(self):
        """Test that create_message() formats the message correctly."""

        class TestRule(FDSRules):
            TEST_RULE = 'Test rule text', 'test_example'

        rule = TestRule.TEST_RULE

        message = rule.create_message()

        expected = 'TEST_RULE: Test rule text (e.g. test_example)'
        assert message == expected

    def test_text_property(self):
        """Test that text property returns the correct value."""

        class TestRule(FDSRules):
            TEST_RULE = 'Test rule text', 'test_example'

        rule = TestRule.TEST_RULE

        assert rule.text == 'Test rule text'

    def test_example_property(self):
        """Test that example property returns the correct value."""

        class TestRule(FDSRules):
            TEST_RULE = 'Test rule text', 'test_example'

        rule = TestRule.TEST_RULE

        assert rule.example == 'test_example'


class TestIntFDSRules:
    """Test IntFDSRules."""

    def test_fds100_rule(self):
        """Test FDS100 rule."""
        rule = IntFDSRules.FDS100
        assert rule.text == 'Group by 3s from right'
        assert rule.example == '10_000'
        assert rule.create_message() == 'FDS100: Group by 3s from right (e.g. 10_000)'


class TestFloatFDSRules:
    """Test FloatFDSRules."""

    def test_fds200_rule(self):
        """Test FDS200 rule."""
        rule = FloatFDSRules.FDS200
        assert rule.text == 'Group by 3s from right'
        assert rule.example == '10_000.1_234'
        assert rule.create_message() == 'FDS200: Group by 3s from right (e.g. 10_000.1_234)'


class TestBinaryFDSRules:
    """Test BinaryFDSRules."""

    def test_fds300_rule(self):
        """Test FDS300 rule."""
        rule = BinaryFDSRules.FDS300
        assert rule.text == 'Group by 4s from right after prefix `0b_`'
        assert rule.example == '0b_1101_1001'
        assert rule.create_message() == 'FDS300: Group by 4s from right after prefix `0b_` (e.g. 0b_1101_1001)'


class TestOctalFDSRules:
    """Test OctalFDSRules."""

    def test_fds400_rule(self):
        """Test FDS400 rule."""
        rule = OctalFDSRules.FDS400
        assert rule.text == 'Group by 3s from right after prefix `0o_`'
        assert rule.example == '0o_12_134_155'
        assert rule.create_message() == 'FDS400: Group by 3s from right after prefix `0o_` (e.g. 0o_12_134_155)'


class TestHexFDSRules:
    """Test HexFDSRules."""

    def test_fds500_rule(self):
        """Test FDS500 rule."""
        rule = HexFDSRules.FDS500
        assert rule.text == 'Group by 4s from right after prefix `0x_`'
        assert rule.example == '0x_CAFE_F00D'
        assert rule.create_message() == 'FDS500: Group by 4s from right after prefix `0x_` (e.g. 0x_CAFE_F00D)'
