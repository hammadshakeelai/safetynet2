pi_value = 3.142857142857143

# 1. Formatting float with different precision
formatted_num = format(pi_value, ".2f")  # Formats the number to 2 decimal places
print(formatted_num)

formatted_num = format(pi_value, ".4f")  # Formats the number to 2 decimal places
print(formatted_num)

# 2. Scientific notation
num = 12345.6789
formatted_num = format(num, ".2e")  # 2 decimal places in scientific notation
print(formatted_num)

# 3. Comma separators
num = 1000000
formatted_num = format(num, ",")  # Adds commas as thousands separators
print(formatted_num)

# 4. Minimum field width
num = 42
formatted_num = format(num, "<5d") # Right-align the integer in a field of width 5
print(formatted_num)
formatted_num = format(num, "5d")  # Implicit is right-align, d for integer
print(formatted_num)

# 5. Percentage
num = 0.1234
formatted_num = format(num, ".2%")  # Converts to percentage with 2 decimal places
print(formatted_num) 

formatted_num = format(num, ".0%")  # Converts to percentage with 2 decimal places
print(formatted_num) 

# 6. Combining format specifiers
num = 1234000.56789
formatted_num = format(num, ",.2f")  # Comma as thousands separator and 2 decimal places
print(formatted_num)