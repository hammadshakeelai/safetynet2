
def change_value(values):
    values[0] = 5
    values.append(40)
    values.insert(1, 15)
    print("Value inside method: ", values)

my_list = [10, 20, 30]
print("Value Before Calling: ", my_list)
change_value(my_list)
print("Value After Calling: ", my_list)

# Python's behavior is context-dependent:
## Immutable objects mimic pass by value.
## Mutable objects mimic pass by reference.
##
## Unlike C++, Python simplifies handling references, as there is no need 
## for explicit syntax (* or &). Be aware of the object type you're working 
## with, as it influences how changes are applied.
