my_dict = {"Name": "Alice", "Roll No": "123", "Address": "Hayatabd"}
for key in my_dict:
    print(key, ": ", my_dict[key], sep="", end=", ")

print("\n------------")
for key in my_dict:
    print(key, ": ", my_dict.get(key), sep="", end=", ")

print("\n------------")
my_dict['Name'] = "Bob"
for key, value in my_dict.items():
    print(key, ": ", value, sep="", end=", ")

## Dictionary: 
#### Unordered: Elements are not stored in a sequence.
#### Unindexed: Element cannot be accessed using its position
#### Mutable/ Changeable: Allowing to add and remove elements after creation.
#### Dynamic Size: The size can grow or shrink dynamically.
#### Heterogeneous: Hold elements of different data types.
#### Uniqueness/ Duplication: No key duplication are allowed.
#### Keyvalue paired: Store data as key-value pairs. 