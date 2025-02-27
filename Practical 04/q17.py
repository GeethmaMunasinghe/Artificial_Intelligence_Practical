def custom_sum(a, b):
    total = a + b
    if 15 <= total <= 20:
        return 20
    return total


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Result:", custom_sum(num1, num2))
