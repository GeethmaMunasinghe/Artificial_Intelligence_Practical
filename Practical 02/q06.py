
def calculate_discounted_price(original_price):
    discount=original_price*0.025
    final_price=original_price-discount
    return final_price

price=float(input("Enter the original price: "))

discounted_price=calculate_discounted_price(price)

print(f"Original Price: ${price:.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")