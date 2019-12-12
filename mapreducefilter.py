from functools import reduce

a = [1, 2, 3, 4, 5, 6]
b = [6, 5, 4, 3, 2, 1]

m = list(map(lambda x, y: x + y, a, b))

print(m)
r = reduce(lambda x, y: x + y, range(1,a))
print(r)
