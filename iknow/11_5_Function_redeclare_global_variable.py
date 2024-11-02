obtained_marks = 90
print("Value before method: ", obtained_marks)

def method():
    # Redeclaring the global variable within the fucntion
    global obtained_marks
    obtained_marks = 10
    print("Value in method: ", obtained_marks)
    
method()
print("Value after method: ", obtained_marks)
