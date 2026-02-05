from items import Item

# INHERITANCE EXAMPLE
class phone(Item):
         def __init__(self, name: str, price: float, quantity: int, broken_phones=0):# Added data types for validation
            # call to super function to access parent class methods
            super().__init__(
                name, price, quantity
            )
            assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
            self.broken_phones = broken_phones

