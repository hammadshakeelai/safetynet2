
def change_value(par_val):
    par_val += 8
    print("Value inside method: ", par_val)
    print("Address inside method: ", id(par_val))
    
my_value = 10
print("Value Before Calling: ", my_value)
print("Address Before Calling: ", id(my_value))
change_value(my_value)
print("Value After Calling: ", my_value)
print("Address After Calling: ", id(my_value))

# In Python, variables are references (or pointers) to objects, 
# not the objects. When you pass a variable to a function, you 
# are passing a reference to the object it points to.

### Immutable vs. Mutable Objects:
## Immutable objects (e.g., int, str, tuple): You cannot modify the object 
# itself. If you try to "modify" it (reassign a value), it creates a new 
# object. This behavior mimics pass by value, because the original variable 
# remains unchanged.

## Mutable objects (e.g., list, dict, set): You can modify the object 
# directly, and changes will reflect outside the function. This behavior 
# mimics pass by reference, as the original object can be changed.

### Note: You create a new reference to another immutable integer object 
# (which, in this case, happens to be the same integer 10 due to interning). 