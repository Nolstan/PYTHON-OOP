# comprehensions are a concise way to create lists, sets, or dictionaries in Python.
# they are often more readable and efficient than traditional loops.
# sytax  [expression for item in iterable if condition]


# Lets start with a traditional loop

double  = []
for i in range(1,11):
    double.append(i*2)
# print(double)

# Now using list comprehension
double_comp = [i * 2 for i in range(1,11) ]
print(double_comp)


# square each number

square = [i**2 for i in range(1,11)]
print(square)


# working with strings
fruits =['banana','mango','guavas']
# fruits = [fruit.upper() for fruit in fruits]

print(fruits)

# traditional for loop
# for fruit in fruits:
#     # print(fruit.upper())

fruit_chars =[fruit[0] for fruit in fruits]
# print(fruit_chars)


numbers = [1,2,-3,4,5,6,-7,8,9,-10]
# to return +ve numbers
positive_nums = [number  for number in numbers if number >= 0]
print(positive_nums)

# To return negative numbers
negative_nums = [number  for number in numbers if number < 0]
print(negative_nums)

# To return Even Numbers
even_nums = [num for num in numbers if num%2 == 0]
print(even_nums)


# ADVANTAGES OF COMPREHENSIONS
# Conciseness: They allow you to create lists in a single line of code.
# Readability: They can make your code more readable by clearly expressing the intent of the operation
# Performance: They can be faster than traditional loops for creating lists.
# Flexibility: They can include conditions to filter items, making them versatile for various use cases.


# LIMITATIONS OF COMPREHENSIONS
# Complexity: Overly complex comprehensions can be hard to read and understand.
# Memory Usage: They create the entire list in memory, which can be inefficient for large datasets.
# Limited Functionality: They are primarily used for creating lists and may not be suitable for all
