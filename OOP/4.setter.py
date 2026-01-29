#  a setter method is used to check if there is a match between
#  what is happening in the code and what we expect to happen


class Item:
    def __init__(self, name: str, price: float, quantity: int):# Added data types for validation

        # validating received values using setter method
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Phone',100,4) # adding a different data type will raise an error
item2 = Item('Laptop',200,5)

print(f"item 1 total price: {item1.calculate_total_price()}")
print(f"item 2 total price: {item2.calculate_total_price()}")


# So far we have been dealing with instance attributes that are public
# Next we move to class attributes