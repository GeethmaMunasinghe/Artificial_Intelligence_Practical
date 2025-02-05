
# List of floating numbers
numbers = [12.345, 98.76, 45.99, 0.567, 123.4]

print("Using round():")
for num in numbers:
    print(round(num))  # Rounds to the nearest integer

print("\nUsing string formatting:")
for num in numbers:
    print(f"{num:.0f}")  # Formats without decimal places

