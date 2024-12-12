def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n-1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]

print(fibonacci(3))

# Recursion is a form of self-referential programming. 
# Recursion can also be referred as 
# Repetitive: 
    # Involves repeating the same logic for smaller subproblems
# Recursive Iteration: 
    # Less common term, it highlights the iterative nature of recursion.
# Divide and Conquer:
    # Follow the divide-and-conquer strategy, a big problem is divided 
    # into smaller problems, solved independently, and then combined.