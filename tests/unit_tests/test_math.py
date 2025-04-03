import pytest
from swap_meet.math import my_max, my_min


def test_my_max_with_key():
    words = ["cat", "kitty", "fish"]

    result = my_max(words, key=len)

    assert result == "kitty"


def test_my_max_with_default_key():
    words = ["cat", "kitty", "fish"]

    result = my_max(words)

    assert result == "kitty"  


def test_my_max_tie_case():
    words = ["cat", "dog", "pet"]

    result = my_max(words, key=len)

    assert result == "cat"


def test_my_max_raises_value_error():
    words = []

    with pytest.raises(ValueError): 
        my_max(words)


def test_my_min_with_key():
    words = ["cat", "kitty", "fish"]

    result = my_min(words, key=len)

    assert result == "cat"


def test_my_min_with_default_key():
    words = ["cat", "kitty", "fish"]

    result = my_min(words)

    assert result == "cat"  


def test_my_min_tie_case():
    words = ["cat", "dog", "pet"]

    result = my_min(words, key=len)

    assert result == "cat"


def test_my_min_raises_value_error():
    words = []

    with pytest.raises(ValueError): 
        my_min(words)
