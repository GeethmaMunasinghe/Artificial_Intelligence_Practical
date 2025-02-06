
price=float(input("Enter the price ($):"))
tax=float(input("Enter the tax (%):"))

net_price=price*tax/100

print(f'The net price is ${net_price}')