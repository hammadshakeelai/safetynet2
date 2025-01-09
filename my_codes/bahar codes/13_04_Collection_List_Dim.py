A = [
        [1, 2,  3,  4], 
        [5, 6,  7,  8], 
        [9, 10, 11, 12]
    ]
rows = 3
cols = 4
print("A = [")
for i in range(rows):
    print("\t[", end="")
    for j in range(cols):
        print(A[i][j], end=", ")
    print("\b\b], ")
print("    ]")
