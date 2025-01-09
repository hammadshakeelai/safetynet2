A = {1, 2, 3, 4, 5}
for item in A:
    print(item, end=", ")

print("\n-----------")
A.add((6,7))
for item in A:
    print(item, end=", ")

print("\n-----------")
A.update((6,7))
for item in A:
    print(item, end=", ")

print("\n-----------")
A.discard((6,7))
for item in A:
    print(item, end=", ")

print("\n-----------")
A.remove(6)
for item in A:
    print(item, end=", ")

## Set: 
#### Unordered: Elements are not stored in a sequence.
#### Unindexed: Element cannot be accessed using its position
#### Mutable/ Changeable: Allowing to add and remove elements after creation.
#### Dynamic Size: The size can grow or shrink dynamically.
#### Heterogeneous: Hold elements of different data types.
#### Uniqueness/ Duplication: No duplicate members are allowed.