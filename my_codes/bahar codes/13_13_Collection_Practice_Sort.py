# Bubble Sort
a = [4, 3, 5, 7, 0, 9, 11, 2]
counter = 0 # Used to check total number of inner operations
size = len(a)
for i in range(size):
    for j in range(size-1-i):
        counter += 1
        if a[j] < a[j+1]:
            temp = a[j] 
            a[j] = a[j+1]
            a[j+1] = temp    
    print(a)
print(counter)