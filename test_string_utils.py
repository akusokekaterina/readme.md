import pytest
from string_utils import StringUtils
@pytest.fixture
def string_utils():
    return StringUtils()
def test_capitalize(string_utils):
    assert string_utils.capitalize("тест") == "Тест"
    assert string_utils.capitalize("тЕст") == "Тест"
    assert string_utils.capitalize("") == ""  # негативный сценарий
    assert string_utils.capitalize(" ") == " "  # негативный сценарий
def test_trim(string_utils):
    assert string_utils.trim("   тест") == "тест"
    assert string_utils.trim("тест   ") == "тест   "
    assert string_utils.trim("  ") == ""  # негативный сценарий
    assert string_utils.trim("") == ""  # негативный сценарий
def test_contains(string_utils):
    assert string_utils.contains("тест", "т") is True
    assert string_utils.contains("тест", "з") is False
    assert string_utils.contains("", "т") is False  # негативный сценарий
    assert string_utils.contains("тест", "") is True  # негативный сценарий
def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("тест", "е") == "тст"
    assert string_utils.delete_symbol("тест", "з") == "тест"  # символа нет
    assert string_utils.delete_symbol("", "т") == ""  # негативный сценарий
    assert string_utils.delete_symbol("тест", "") == "тест"  # негативный сценарий
