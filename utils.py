def max_value(arr):
    if not arr:
        return None
    return max(arr)

def is_palindrome(s):
    clean = ''.join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))
