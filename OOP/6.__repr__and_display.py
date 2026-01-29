
class Item:
    pay_rate = 0.8# An example of a class attribute
    All = [] # to keep track of all instances created
    def __init__(self, name: str, price: float, quantity: int):# Added data types for validation
     
        # validating received values using setter method
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.All.append(self) # to keep track of all instances created


    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"  

# Adding more items
item1 = Item('Phone',100,4) # adding a different data type will raise an error
item2 = Item('Laptop',200,5)
item3 = Item('Tablet',150,3)
item4 = Item('Monitor',300,2)
item5 = Item('Keyboard',50,10)
item6 = Item('Mouse',25,8)

# representing all items created so far
print('\n REPRESENTATION OF ALL ITEMS CREATED SO FAR USING __repr__:\n')
print(f'{Item.All} \n')

# print all items created so far
for item in Item.All:
    print(f"Item: {item.name}, Price: {item.price}, Quantity: {item.quantity}")


# FOR GOOD PRACTICE KEEP THE VALUES IN CSV FORMAT
# THIS WILL HELP WHEN SAVING TO A FILE OR DATABASE LATER
# Next Example