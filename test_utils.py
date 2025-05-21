from utils import max_value, is_palindrome, remove_duplicates

def test_max_value():
    assert max_value([1, 5, 3]) == 5
    assert max_value([]) is None

def test_is_palindrome():
    assert is_palindrome("arara") is True
    assert is_palindrome("banana") is False
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([]) == []
