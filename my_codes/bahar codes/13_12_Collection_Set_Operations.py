A = {1, 2, 3, 4}
B = {3, 4, 5}

print("\n----- Union ------")
C = A | B # OR
C = A.union(B) 
for item in C:
    print(item, end=", ")

print("\n----- Intersection ------")
C = A & B # OR
C = A.intersection(B) 
for item in C:
    print(item, end=", ")

print("\n----- Set Difference ------")
C = A - B # OR
C = A.difference(B) 
for item in C:
    print(item, end=", ")

print("\n----- Exclusive OR | XOR ------")
C = A ^ B # OR
C = A.symmetric_difference(B) 
for item in C:
    print(item, end=", ")