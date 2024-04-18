def generatePrimes(n):
    # Initialize a list to track prime numbers
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    # Apply Sieve of Eratosthenes algorithm
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    # Generate prime numbers
    prime_numbers = [i for i in range(2, n+1) if primes[i]]

    return prime_numbers