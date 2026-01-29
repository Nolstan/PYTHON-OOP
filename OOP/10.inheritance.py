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
        return f"Item('{self.name}',{self.price},{self.quantity})"
    

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

# INHERITANCE EXAMPLE
class phone(Item):
         All = []
         def __init__(self, name: str, price: float, quantity: int, broken_phones=0):# Added data types for validation
     
            # validating received values using setter method
            assert price >= 0, f"Price {price} is not greater than or equal to zero!"
            assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
            assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
            self.name = name
            self.price = price
            self.quantity = quantity
            self.broken_phones = broken_phones

            phone.All.append(self) # to keep track of all instances created

phone1 = phone('iPhone',1000,5,1)
print(f'Total price for phone 1: { phone1.calculate_total_price()}' )
phone2 = phone('Samsung',900,4,2)

# Will continue inheritance in the next file with super() function