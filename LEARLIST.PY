fruits = ["apple", "banana", "cherry"]

# Adding an element
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Inserting an element at index 1
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# Removing an element
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange']

# Popping an element
fruits.pop(2)
print(fruits)  # Output: ['apple', 'kiwi', 'orange']

# Sorting a list
numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 4, 9]

# Reversing a list
numbers.reverse()
print(numbers)  # Output: [9, 4, 2, 1]
# Generate a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Yes, apple is in the list")
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3