def is_in_range(number, start, end):
    """Check if a number falls within a given range [start, end]."""
    return start <= number <= end

# Example usage:
print(is_in_range(5, 1, 10))  # Output: True
print(is_in_range(15, 1, 10)) # Output: False
