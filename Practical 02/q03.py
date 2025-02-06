

def calculate_result(number1, number2):
    product = number1 * number2
    if product<=1000:
        return product
    else:
        return number1+number2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


output=calculate_result(number1,number2)
print("Output:",output)
