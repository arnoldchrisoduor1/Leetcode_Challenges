def print_largest_prime_factor(n):
    """
    Print the largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    print(n)

print_largest_prime_factor(600851475143)