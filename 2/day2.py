def isPrime(n):

    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


N = 5433000 - 1
gifts = 0
primes = []

for i in range(0, 100):

    if (isPrime(i) == True):
        primes.append(i)
    if "7" in str(i):
        if isPrime(i) == True:
            gifts -= i + 1
        else:
            gifts -= primes[len(primes) - 1]
    else:
        gifts = gifts + 1

    print(i, gifts)
print(primes)
print(isPrime(27))
