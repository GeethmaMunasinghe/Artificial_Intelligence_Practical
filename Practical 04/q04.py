
inputnumbers=int(input("Enter a number: "))

if inputnumbers<=1:
    print("Not Prime Number")
else:
    is_prime=True
    for i in range(2,inputnumbers):
        if inputnumbers%i==0:
            is_prime=False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")
