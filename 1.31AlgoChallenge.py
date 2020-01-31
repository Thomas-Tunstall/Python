for a in range(1, 1000):
    for b in range(1, 1000):
        if b > a:
            for c in range(1, 1000):
                if c > b:
                    if (a**2) + (b**2) == (c**2):
                        if a + b + c == 1000:
                            product = (a+b+c)
                            print(f"product a:{a}, b:{b}, c:{c}")
                            print(product)