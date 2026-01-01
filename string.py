def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def is_valid_palindrome(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]

def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
