for a in range(0, 334):
    for b in range(a, 500):
        c = 1000 - a - b

        if a * a + b * b == (1000 - a - b) * (1000 - a - b):
            print a, b, c
