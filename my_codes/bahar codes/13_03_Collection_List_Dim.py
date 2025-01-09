A = [
        [1, 2,  3,  4], 
        [5, 6,  7,  8], 
        [9, 10, 11, 12]
    ]
rows = 3
cols = 4
for i in range(rows):
    for j in range(cols):
        print(f"({i}, {j}) = {A[i][j]}")