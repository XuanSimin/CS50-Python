from plates import is_valid


def test_letter_starts():
    assert is_valid("FR4")
    assert not is_valid("F34563")


def test_only_letters():
    assert is_valid("China")
    assert is_valid("USA")


def test_firstnumber0():
    assert not is_valid("DEF0123")
    assert is_valid("DEF12")


def test_length():
    assert is_valid("China1")
    assert not is_valid("China12")


def test_others():
    assert not is_valid("China?")
    assert not is_valid("Chi2f")
