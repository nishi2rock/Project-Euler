# This approach is taking very long if I add another 0
inputNum = 1000000
n = inputNum + 1 # (d + n / d), when d = 1, could be a prime

primes = range(3, n + 1, 2)
size = len(primes)

for pos, fac in enumerate(primes):
    if fac != 0:
        for idx in range(pos + fac, size, fac):
            primes[idx] = 0

primes = set(primes)
primes.add(2)

def isPrime(n):
    global primes
    return n in primes

def divsAddToPrimes(n):
    fac = 1
    while fac * fac <= n:
        if num % fac == 0:
            if not isPrime(fac + n / fac):
                return False
        fac += 1
    return True

s = 0
for num in range(2, inputNum, 2):
    if divsAddToPrimes(num):
        s += num

print s

