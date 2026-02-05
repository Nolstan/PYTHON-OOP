# generator expressions are similar to list comprehensions, but they use parentheses instead of square brackets.
# they generate items on-the-fly and are more memory efficient for large datasets.
# on-the-fly means they generate items one at a time and only when requested, rather than storing the entire list in memory.
# they are often used in place of list comprehensions when working with large datasets.
# syntax  (expression for item in iterable if condition)

# number = int(input("Enter a number to count to: "))
# counter = (i for i in range(1,number+1))
# print(counter)

# for num in counter:
    # print(num)

# we can use generators to read files fast
#  file_name = 'test.txt'

# with open(file_name,'r') as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)


# square every numb

number = int(input("Enter a number to square even up to: "))

even_square = (num**2 for num in range(1,number+1) if num%2 ==0)
# print(square)

for num in even_square:
    print(num)



# The advantages of using generator expressions include:
# Memory Efficiency: They generate items on-the-fly, which is more memory efficient for large datasets.
# Lazy Evaluation: Items are produced only when requested, which can lead to performance improvements.
# Improved Readability: They provide a concise and readable way to create iterators.
# Flexibility: They can be used in place of list comprehensions when working with large datasets.

# However, they also have some limitations:
# Single Iteration: Once a generator is exhausted, it cannot be reused or reset.
# Limited Use: They are not suitable for all use cases.