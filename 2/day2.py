# basic prime finder from GeeksforGeeks
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


def findClosestPrime(n):
    while not isPrime(n):
        n -= 1
    return n


N = 5433000
gifts = 0
currentPrime = 0
i = 0
deliveredGifts = []

while i < N:
    if "7" in str(i):
        i += findClosestPrime(i)
    else:
        gifts += 1
        deliveredGifts.append(i)
    i += 1

# print(deliveredGifts)
print("delivered gifts:", gifts)
