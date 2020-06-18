from random import choice


def coin_flip():
    return choice(['heads', 'tails'])


print(coin_flip())


def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0]


print(generate_evens())


def square(num):
    return num * num


print(square(8))


def exponent(num, power=2):
    return num ** power


print(exponent(2))
