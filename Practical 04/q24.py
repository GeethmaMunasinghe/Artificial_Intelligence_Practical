def print_even_numbers(numbers):
    """Print all even numbers from the given list."""
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)

# Example usage:
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(sample_list)
