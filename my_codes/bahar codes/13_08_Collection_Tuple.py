my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item, end=" ")
my_tuple[0] = 100   # Does not support item assignment 
#my_tuple.append()  # You cannot add

## Tuple: 
#### Ordered: Elements are stored in a specific sequence.
#### Indexed: Each element can be accessed using its position (index).
#### Immutable: No Allowing to add and remove elements after creation.
#### Heterogeneous: Hold elements of different data types.
#### Uniqueness/ Duplication: Allows duplicate members.