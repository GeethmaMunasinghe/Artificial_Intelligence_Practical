def is_all_even(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

even_numbers = [str(num) for num in range(100, 401) if is_all_even(num)]

print(",".join(even_numbers))
