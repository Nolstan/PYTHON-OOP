# By adding validation to our inputs we can avoid errors when creating objects
# This solves the problem mentioned in the previous example

class Item:
    def __init__(self, name: str, price: float, quantity: int):# Added data types for validation
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Phone',100,4) # adding a different data type will raise an error
item2 = Item('Laptop',200,5)

print(f"item 1 total price: {item1.calculate_total_price()}")
print(f"item 2 total price: {item2.calculate_total_price()}")

# To avoid problems like passing Negative values we can add further validation
# Using the setter method in the next example