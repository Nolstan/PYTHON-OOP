# Now with __init__ function
# Adv
# Object is always ready to use
# Setup is automatic
# Errors prevented early
# Structured initialization

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Phone',100,4)
item2 = Item('Laptop',200,5)

print(f"item 1 total price: {item1.calculate_total_price()}")
print(f"item 2 total price: {item2.calculate_total_price()}")

# The problem with this method is that if we pass in strings we wont catch errors
# We will address this in the next example with data validation