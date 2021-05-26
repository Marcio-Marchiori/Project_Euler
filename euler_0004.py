l = []
for x in range(1000):

    for y in range(1000):
        str_s= x*y
        s = str(str_s)
        first_half  = s[:len(s)//2]
        second_half = s[len(s)//2:][::-1]
        if first_half == second_half:
            l.append((x,y))

cv = []
for i in l:
    cv.append(i[0]*i[1])
print(max(cv))