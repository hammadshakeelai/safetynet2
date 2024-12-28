total_marks = 120
marks_list = [95, 85, 92, 87, 65] # List: Collection Type

for marks in marks_list:
    print("Marks obtained: ", marks)
    print("Total Marks: ", total_marks)
    print("Percentage: ",round((marks/total_marks)*100, 2))

# Accessing value at specific index (Indexing starts from 0)
print(marks_list[2]) 

# range(start, end, step), default start and step value is 0 
# range(3) => [0, 1, 2]                 end value is excluded
# range(1, 3) => [1, 2]                 start = 1
# range(0, 10, 2) => [0, 2, 4, 6, 8]     step = 2

for index in range(3): # range(3) => [0, 1, 2]
    print("Marks obtained: ", marks_list[index])
    print("Total Marks: ", total_marks)
    print("Percentage: ",round((marks_list[index]/total_marks)*100, 2))

for i in range(100, 0, -5):
    print(i, end=", ")

sum = 0
for i in range(1, 101):
    sum = sum + i
print("\nTotal oranges: ", sum)

fact = 1
for i in range(1, 7):
    fact = fact * i
print("\nFactorial: ", fact)

fact = 1
for i in range(6, 0, -1):
    fact = fact * i
print("Factorial: ", fact)