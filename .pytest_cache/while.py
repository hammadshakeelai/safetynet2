i=int(input("enter prime number"))
while i %  2==1:
    print("doremon")
    i=int(input("enter prime number : "))
i = 0

while i < 5:
    print(i)
    i += 1
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
i = 0
while i < 3:
    print("Loop with Else:", i)
    i += 1

else:
    print("Loop finished!")
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping iteration when i is", i)
        continue
    print("Loop with Continue:", i)