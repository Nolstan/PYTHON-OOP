import csv
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
    
    # staticmethod does not take cls or self as first argument
    # this is because static methods do not operate on an instance or class
    # They act like any other isolated function but belong to the class's namespace
    @staticmethod
    def is_interger(num):
         
         if isinstance(num,float):#checking if num value is int
              return num.is_integer()
         elif isinstance(num,int):
              return True
         else:
              return False


    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}',{self.price},{self.quantity}"
    

    @classmethod #decorator to define a class method
    def instantiate_from_csv(cls):
        with open('OOP/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
                # This creates an instance, triggering __init__ which appends to Item.All
                cls(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity = int(item.get('quantity'))
                )

