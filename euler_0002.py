x = 1
y = 2
z = 0
fibo_num = [1,2]

while z < 4000000:
    z = x + y
    if z < 4000000:
       fibo_num.append(z)
    x = y
    y = z
    
total = [x for x in fibo_num if x % 2 == 0]

print(sum(total))