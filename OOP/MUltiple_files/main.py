from items import Item
from  phone import phone    


# Item.instantiate_from_csv()
# print(Item.All)

# for encapsulation example
item1  =Item("Laptop",1000,3)
print(item1.name)
# But if we try to change the name directly
item1.name = "New Laptop" #using setter this will work with restrictions given in setter method
# its not gonna change because we have not provided any setter method to change it
print(item1.name) # still prints New Laptop with the use of setter method



# IF WE USE GETTERS TO MAKE VALUES READONLY
# WHY USE SETTERS THEN?
# Because sometimes we might want to change the value but with some restrictions
# that are achievable through setters
# FOR EXAMPLE WE MIGHT WANT TO RESTRICT THE NAME TO A CERTAIN LENGTH
