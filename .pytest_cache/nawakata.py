# 4. Minimum field width
num = 42
formatted_num = format(num, "<5d") # Right-align the integer in a field of width 5
print(formatted_num,"ghjj")
formatted_num = format(num, "5d")  # Implicit is right-align, d for integer
print(formatted_num,"jj",sep="_")