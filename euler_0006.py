sum_sqrd = sum([x**2 for x in range(1,101)])
sum_to_sqrd = sum([x for x in range(1,101)])**2
result = sum_to_sqrd-sum_sqrd
print(result)