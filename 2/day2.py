def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


N = 5433000 - 1
gifts = 0
primes = []

for i in range(0, 19):
    if (isPrime(i) == True):
        primes.append(i)
    if "7" in str(i):
        if isPrime(i):
            gifts -= i + 1
        else:
            gifts -= primes[len(primes) - 1]
    else:
        gifts = gifts + 1

    print(i, gifts)
print(primes)
print(isPrime(27))
