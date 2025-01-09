def my_function(num):
    print(num)
    if num == 10:
        return
    
    my_function(num + 1)

f = my_function(1)

# Recursion is a form of self-referential programming. 
# Recursion can also be referred as 
# Repetitive: 
    # Involves repeating the same logic for smaller subproblems
# Recursive Iteration: 
    # Less common term, it highlights the iterative nature of recursion.
# Divide and Conquer:
    # Follow the divide-and-conquer strategy, a big problem is divided 
    # into smaller problems, solved independently, and then combined.
