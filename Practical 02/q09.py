

def int_to_binary_with_leading_zeros(number, bit_length=8):
    binary_representation = format(number, f'0{bit_length}b')
    return binary_representation

num = int(input("Enter an integer: "))

bit_length = int(input("Enter the bit length (e.g., 8 for 8-bit, 16 for 16-bit): "))

binary_output = int_to_binary_with_leading_zeros(num, bit_length)
print(f"Binary representation with leading zeros ({bit_length}-bit): {binary_output}")
