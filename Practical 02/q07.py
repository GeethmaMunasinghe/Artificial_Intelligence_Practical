previous_number=0

print("Print the sum of current and previous number")

for current_number in range(10):
    sum_numbers=previous_number+current_number
    print(f"Current Number:{current_number}, Previous Number:{previous_number}, Sum:{sum_numbers}")
    previous_number=current_number