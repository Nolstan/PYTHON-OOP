# 1. Lists
# Used for general-purpose storage of ordered collections of items.
# Can grow and shrink dynamically.(Mutable)
# sortable and indexable.

# 2. Tuples
# they are useful for storing fixed collections of items.
# Immutable and can be used as keys in dictionaries.
# sortable and indexable
# faster than lists.

# 3. Sets
# they are useful for storing unique items.
# Immutable and can be used as keys in dictionaries.
# unordered
# very fast vs lists and tuples for membership testing.

# 4. Dictionaries
# they are useful for storing key-value pairs.
# Mutable and can grow and shrink dynamically.
# unordered
# very fast vs lists and tuples for membership testing.

# JUST FOR FUN
# x  = [z**2 for z in range(10) if z>4]
# print(x)


# LIST Example
my_list = [1, 2, 3, 4, 5,'Nolstan']
# print(f'My List: {my_list}')

# Lists functions

# Append - adds an item to the end of the list
my_list.append(6)
# print(f'After Append: {my_list}')

# Extend - adds multiple items to the end of the list
my_list.extend([7, 8, 9])
# print(f'After extend: {my_list}')

# Insert - adds an item at a specific index
my_list.insert(1, "Malani") #insert "Malani" at index 1
# print(f'After insert: {my_list}')

# Remove - removes an item from the list
my_list.remove(3) #removes the first occurrence of 3
# print(f'After remove: {my_list}')

# Pop - removes an item from the list   
popped_item = my_list.pop() #removes the last item
# print(f'After pop: {my_list}, Popped Item: {popped_item}')

# del - removes an item at a specific index
del my_list[0] #removes the item at index 0
# print(f'After del: {my_list}')

# The difference between remove, pop, and del is that 
# remove removes a specific item by value, 
# pop removes an item by index and returns it
# del removes an item by index without returning it.

# SLINCING IN LISTS
# Slicing allows you to extract a portion of a list by specifying a start and end index

print(f'Original List: {my_list}')

print(f'First three items: {my_list[:3]}')

print(f'Last three items: {my_list[-3:]}')

print(f'Excluding last three items: {my_list[:-3]}')

# Skipping items
print(f'Every second item: {my_list[::2]}')
print(f'{my_list[:5:2]}')  # First four items with step of 2   

# to print the list in reverse order
print(f'Reversed List: {my_list[::-1]}')


# SORT vs SORTED
unsorted_list = [5, 2, 9, 1, 5, 6]

# using sorted() function
sorted_list = sorted(unsorted_list)
print(f'Sorted List: {sorted_list}')
print(f'Original Unsorted List: {unsorted_list}')

# using sort() method
unsorted_list.sort()
print(f'Sorted Unsorted List using sort(): {unsorted_list}')
print(f'Original Unsorted List after sort(): {unsorted_list}')

# The difference between sort() and sorted() is that
# sort() modifies the original list in place and returns None,
# while sorted() creates a new sorted list and leaves the original list unchanged.

# Sorting in descending order
unsorted_list.sort(reverse=True)
print(f'Sorted Unsorted List using sort(): {unsorted_list}')








# TUPLE Example
# declaring a tuple
my_tuple = (1, 2, 3, 4, 5,'Nolstan') # tuple is declared using parentheses ,matter of fact even without parentheses
# print (f'My Tuple: {my_tuple}')

# Adding items to a tuple is not possible since tuples are immutable.
# However, you can concatenate two tuples to create a new tuple.
new_tuple =my_tuple + (6, 7, 8,'Beatrice') #concatenating two tuples
print(f'New tuple after concatenation: {new_tuple}')





# DICTIONARY Example

anime_dict = {
    1: 'Naruto',
    2: 'One Piece',
    3: 'Attack on Titan',
    4: 'Bleach',
    5: 'Death Note'
}

print(f'Original Dictionary: {anime_dict}')

# changing values in dictionary
anime_dict[3] = 'Fullmetal Alchemist' #changing value at key 3
print(f'After changing value at key 3: {anime_dict}')

# adding new key-value pair
anime_dict[6] ='My Hero Academia'
anime_dict[7] = 'Demon Slayer' #adding new key-value pair

print(f'After adding new key-value pairs: {anime_dict}')

# removing key-value pair
removed_value = anime_dict.pop(6) #removing key-value pair at key 2
print(f'After removing key 2: {anime_dict}, Removed Value: {removed_value}')

# using del to remove key-value pair
del anime_dict[1] #removing key-value pair at key 1
print(f'After deleting key 1: {anime_dict}')

# NOTE: there is no remove() method for dictionaries like there is for lists .
# That's because dictionaries are not ordered collections of items like lists are.

# ACCESSING DICTIONARY keys
print(f'Keys in Dictionary: {anime_dict.keys()}')

# ACCESSING DICTIONARY values
print(f'Values in Dictionary: {anime_dict.values()}')

# ACCESSING DICTIONARY items
print(f'Items in Dictionary: {list(anime_dict.items())}') # wrapped in list for better readability like list(anime_dict.items())










# SET Example
my_set = {1, 2, 3, 4, 5} # set is declared using curly braces
print(f'Original Set: {my_set}')

# Adding items to a set
my_set.add(6) #adding single item
print(f'After adding 6: {my_set}')

my_set.update([7, 8, 9]) #adding multiple items
print(f'After adding multiple items: {my_set}')# output of myset is [1,2,3,4,5,6,7,8,9]

# FUNCTIONS ON SETS

# Union - combines two sets and eliminates duplicates
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(f'Union of set_a and set_b: {union_set}')

# Intersection - returns only the items that are present in both sets
intersection_set = set_a.intersection(set_b)
print(f'Intersection of set_a and set_b: {intersection_set}')

# Difference - returns the items that are present in the first set but not in the second set
difference_set = set_a.difference(set_b)
print(f'Difference of set_a and set_b: {difference_set}')

# Symmetric Difference - returns the items that are present in either set but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f'Symmetric Difference of set_a and set_b: {symmetric_difference_set}')

# Discard - removes an item from the set if it is present
my_set.discard(3) #removes 3 if present
print(f'After discarding 3: {my_set}')

# Remove - removes an item from the set, raises KeyError if item not present
my_set.remove(20) #removes 2
print(f'After removing 20: {my_set}') # This will raise an error since 20 is not in the set
