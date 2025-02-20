import string

def is_pangram(sentence):
    """Check if a sentence is a pangram (contains all letters A-Z)."""
    alphabet_set = set(string.ascii_lowercase)
    return alphabet_set.issubset(set(sentence.lower()))

# Example usage:
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
print(is_pangram("Hello World"))  # Output: False
