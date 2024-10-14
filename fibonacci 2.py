
n = 11   # Number of Fibonacci numbers to generate

fibonacci = 1   # Initialize the first two Fibonacci numbers
g = 1

print(fibonacci)
print(g)# Print the first two numbers

# Generate and print the rest of the Fibonacci sequence
for _ in range(n - 2):
    next_fib = fibonacci + g
    print(next_fib)
    
    # Update for the next iteration
    fibonacci, g = g, next_fib


   