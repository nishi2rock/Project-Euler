def largestPrimeFactor(n):
    f = 1
    while n > 1:
        f += 1
        while n % f == 0:
            n = n / f
    return f
