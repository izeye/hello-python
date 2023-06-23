def double(n):
    return n * 2


numbers = (1, 2, 3, 4)
doubled = map(double, numbers)
print(list(doubled))
