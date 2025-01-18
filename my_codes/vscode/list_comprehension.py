print([x**2 for x in range(10)])
print([x for x in range(10) if x % 2 == 0])
print([(x, y) for x in range(3) for y in range(3)])
words = ["hello", "world"]
print([word.upper() for word in words])
print( [x for x in range(20) if x % 2 == 0 and x % 3 == 0])