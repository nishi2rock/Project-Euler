fibs = []

a = 1
b = 1
while b < 4000000:
    fibs.extend([a, b])
    a += b
    b += a

if a < 4000000:
    fibs.append(a)

print sum(fibs[2::3])
