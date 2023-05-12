def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)

def fibonacci_sequence(n):
    i = 0
    while(fibonacci(i) <= n):
        print(fibonacci(i))
        i += 1
        
fibonacci_sequence(10)

# Initialize variables
a, b = 1, 2
sum = 0

# Generate Fibonacci sequence and add even-valued terms
while a <= 4000000:
    if a % 2 == 0:
        sum += a
    a, b = b, a + b

# Print the sum of even-valued terms
print(sum)