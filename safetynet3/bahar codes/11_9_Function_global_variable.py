## Redeclaring Global Variable
my_global_variable = 90
def add():
    global my_global_variable # comment to see the effect
    # Without using the global keyword, the local variable will be created below 
    my_global_variable = 80 
    print(my_global_variable)

print(my_global_variable)
add()
print(my_global_variable)