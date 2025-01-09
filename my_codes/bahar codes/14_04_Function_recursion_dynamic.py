def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n-1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]

print(fibonacci(60)) 

# Major issue with the recursion is the space complexity
# The space complexity can be reduced. 
    # 1. Using dynamic programming (e.g., memoization) 
    # 2. Converting recursion to iteration.