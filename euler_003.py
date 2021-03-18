x = 600851475143

while x > 1:
    for i in range(1,600851475143):
        if x % i == 0:
            x = x/i
            print(x)
