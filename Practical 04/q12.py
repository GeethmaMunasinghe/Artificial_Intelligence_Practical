# Get input from the user
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))

# Find the median using sorting
median = sorted([num1, num2, num3])[1]

# Display the result
print("The median is", median)
