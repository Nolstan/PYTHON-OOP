# A class attribute is an attribute that is shared among all instances of a class

class Item:
    pay_rate = 0.8# An example of a class attribute
    def __init__(self, name: str, price: float, quantity: int):# Added data types for validation

        # validating received values using setter method
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('Phone',100,4) # adding a different data type will raise an error
item2 = Item('Laptop',200,5)

#  __dict__ shows the attributes of an instance
# print(Item.__dict__) # shows the class attributes
# print(item1.__dict__) # shows the instance attributes

# APPLY DISCOUNT
print(f"item 1 price before discount: {item1.price}")
item1.apply_discount()
print(f"item 1 price after discount: {item1.price}")

# what if u want to apply a different discount to a different instance
item2.pay_rate = 0.7 # this creates an instance attribute that overrides the class attribute for this instance only
print(f"item 2 price before discount: {item2.price}")
item2.apply_discount()
print(f"item 2 price after discount: {item2.price}")

# At this point i im able to tell the difference between class attributes level and instance attributes level
# Its a must to know



# Now currently we do not have an approach to get all items created
# We will address this in the next example using class methods