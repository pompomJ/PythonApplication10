def isprime(n):
    prime = True
    for i in range(2, n/2):
        if n % i == 0:
            prime = False
            break
        return prime

