
Value = 2 + 2 * 2
print("Value: ", Value)

print("Changing precedence using parenthesis")
Value = (2 + 2) * 2
print("Value: ", Value)

print("Default Order")
Value = 2 + 4 / 2 * 2**3  
#     = 2 + 4 / 2 * 8  
#     = 2 + 4 / 2 * 8  
#     = 2 + 2 * 8  
#     = 2 + 16  
#     = 18  
print("Value: ", Value)
