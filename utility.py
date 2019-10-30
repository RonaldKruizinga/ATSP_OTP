from random import randint
from random import getrandbits


def get_random_number():
    return randint(1, 10000)


def get_random_number_with_max(maximum):
    return randint(0, maximum-1)


def get_random_bit():
    return randint(0, 1)


# The below from cryptography/Diffie-Hellman

def is_prime_calc(num):
    return all(num % i for i in range(2, num))


def is_prime(num):
    return is_prime_calc(num)


def get_random_prime():
    while True:
        n = getrandbits(12) + 3
        if is_prime(n):
            return n


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def primitive_root(modulo):
    required_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            return g


