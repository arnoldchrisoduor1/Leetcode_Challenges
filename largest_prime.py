def print_primes(n):
    """
    Print all prime numbers up to n.
    """
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

print_primes(50)