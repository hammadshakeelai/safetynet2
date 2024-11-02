# Printing basic String 
print("Hello World!") 

# Printing variables 
a = 10
b = 20
c = a + b
print(a, "+", b, "=", c) 

# Printing Multiple Items
# By default, print() separates items with a space
print("Name:", "Alice", "Age:", 25)

# Using the sep Parameter to change default separater
print("apple", "banana", "cherry", sep=", ")

# By default, print() ends with a newline
print("This is print 1.") # add \n at the end
print("This is print 2.")

# Using the end Parameter to change default \n
print("This is print 1.", end=" ")
print("This is print 2.")