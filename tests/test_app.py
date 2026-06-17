from app import is_newer, normalize_name


def test_is_newer_true():
    assert is_newer("3.13", "3.11") is True


def test_is_newer_false():
    assert is_newer("3.10", "3.11") is False


def test_normalize_name():
    assert normalize_name("  neil chaudhari  ") == "Neil Chaudhari"
