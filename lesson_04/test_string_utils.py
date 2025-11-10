import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('text, expected', [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python")
])
def test_capitalize_positive(text, expected):
    assert string_utils.capitalize(text) == expected


@pytest.mark.positive
@pytest.mark.parametrize('text, expected', [
    ("  Skypro", "Skypro"),
    ("  text with backspace", "text with backspace"),
    ("  123", "123")
])
def test_trim_positive(text, expected):
    assert string_utils.trim(text) == expected


@pytest.mark.positive
@pytest.mark.parametrize('text, symbol', [
    ("Skypro", "S"),
    ("text with backspace", "w"),
    ("123", "3")
])
def test_contains_positive(text, symbol):
    assert string_utils.contains(text, symbol) is True


@pytest.mark.positive
@pytest.mark.parametrize('text, symbol, expected', [
    ("Skypro", "Sk", "ypro"),
    ("text with backspace", "with", "text  backspace"),
    ("123", "3", "12")
])
def test_delete_symbol_positive(text, symbol, expected):
    assert string_utils.delete_symbol(text, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('text, expected', [
    ("123abc", "123abc"),
    ("", ""),
    ("  ", "  ")
])
def test_capitalize_negative(text, expected):
    assert string_utils.capitalize(text) == expected


@pytest.mark.negative
def test_capitalize_with_none():
    with pytest.raises(TypeError):
        string_utils.capitalize(None)


@pytest.mark.negative
@pytest.mark.parametrize('text, expected', [
    ("Skypro", "Skypro"),
    ("", "")
])
def test_trim_negative(text, expected):
    assert string_utils.trim(text) == expected


@pytest.mark.negative
@pytest.mark.parametrize('text, symbol', [
    ("Skypro", "U"),
    ("", "z"),
    ("123", "")
])
def test_contains_negative(text, symbol):
    assert string_utils.contains(text, symbol) is False


@pytest.mark.negative
@pytest.mark.parametrize('text, symbol, expected', [
    ("Skypro", "You", "Skypro"),
    ("123", "4", "123"),
    ("text with backspace", "", "text with backspace")
])
def test_delete_symbol_negative1(text, symbol, expected):
    assert string_utils.delete_symbol(text, symbol) == expected
