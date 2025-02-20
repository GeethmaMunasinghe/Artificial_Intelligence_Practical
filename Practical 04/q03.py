
number=int(input("Enter the number: "))

print(f"Divisors of {number} are: ")
for i in range(1,number+1):
    if number % i==0:
        print(i)