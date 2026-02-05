import csv
class Item:
    pay_rate = 0.8# An example of a class attribute
    All = [] # to keep track of all instances created
    def __init__(self, name: str, price: float, quantity: int):# Added data types for validation
     
        # validating received values using setter method
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.__name = name # private attribute(encapsulated)
        self.__price = price
        self.quantity = quantity

        Item.All.append(self) # to keep track of all instances created
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.price * self.pay_rate
    def apply_increment(self):
        self.__price = self.price + self.price * self.pay_rate
    @property
    def name(self):
        return self.__name # getter method to access private attribute
    
    @name.setter #setter method to allow updating private values
    def name(self,value):
         if len(value) > 10:
              raise Exception("The name is too long!")  
         self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity
    

    
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
                    price = float(item.get('__price')),
                    quantity = int(item.get('quantity'))
                )

# What encapsulation does is to restrict access to methods and variables
# to prevent data from being modified accidentally
 
 
# IF WE USE GETTERS TO MAKE VALUES READONLY
# WHY USE SETTERS THEN?
# Because sometimes we might want to change the value but with some restrictions
# that are achievable through setters
# FOR EXAMPLE WE MIGHT WANT TO RESTRICT THE NAME TO A CERTAIN LENGTH


# The same information is in main.py 