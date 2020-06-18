def cube(num): return num ** 3


print(cube(2))


def decrement_list(numbers):
    return list(map(lambda num: num - 1, numbers))


print(decrement_list([1, 2, 3]))


def remove_negatives(numbers):
    return list(filter(lambda num: num > 0, numbers))


print(remove_negatives([-1, 3, 4, -99]))
