my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item, end=" ")
print()

my_list[0] = 100    # You can change value
my_list.append(200) # You can add value
for item in my_list:
    print(item, end=" ")

# When choosing a collection type, it is useful to understand the properties of that type.

## List: 
#### Ordered: Elements are stored in a specific sequence.
#### Indexed: Each element can be accessed using its position (index).
#### Mutable/ Changeable: Allowing to add and remove elements after creation.
#### Dynamic Size: The size can grow or shrink dynamically.
#### Heterogeneous: Hold elements of different data types.
#### Uniqueness/ Duplication: Allow duplicate members.

### For difference consider these points
# Mutability: Allowing you to add and remove elements after creation.
# Uniqueness: Storing unique elements. Duplicate elements are automatically eliminated.
# Ordering: The elements are stored in any particular sequence. Can use Indexing to access individual element
# Keyvalue paired: Store data as key-value pairs. 
