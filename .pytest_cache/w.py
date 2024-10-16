# Example of a basic while loop
i = 0
while i < 5:
    print("Basic Loop:", i)
    i += 1  # Increment to avoid infinite loop

# Example of an infinite loop (commented out to avoid execution)
# while True:
#     print("This would run forever!")

# Breaking out of a while loop
i = 0
while i < 10:
    if i == 5:
        print("Breaking out of the loop when i is", i)
        break
    print("Loop with Break:", i)
    i += 1

# Using continue in a while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping iteration when i is", i)
        continue
    print("Loop with Continue:", i)

# Using else with a while loop
i = 0
while i < 3:
    print("Loop with Else:", i)
    i += 1
else:
    print("Loop finished!")

# Example to demonstrate pitfalls (this loop would run forever without increment)
# i = 0
# while i < 3:
#     print("Infinite Loop Example:", i)
#     # The missing increment of i would cause an infinite loop
