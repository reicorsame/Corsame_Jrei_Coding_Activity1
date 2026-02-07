cart = {'apple': 2, 'banana': 5, 'milk': 1}

item = input("Enter an item to add to the cart: ").lower()

# Update the cart
if item in cart:
    cart[item] += 1
else:
    cart[item] = 1

print("\nUpdated shopping cart:")
for item, count in cart.items():
    print(f"{item}: {count}")
