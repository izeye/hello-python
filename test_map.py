def double(n):
    return n * 2


numbers = (1, 2, 3, 4)
doubled = map(double, numbers)
print(list(doubled))


def to_person(s):
    return {'name': s}


names = ('Johnny', 'John')

persons = map(to_person, names)
print(list(persons))

persons = map(lambda name: {'name': name}, names)
print(list(persons))
