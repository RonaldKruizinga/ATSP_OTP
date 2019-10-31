import math
from random import randint
from random import getrandbits


def get_random_number():
    return randint(1, 10000)


def get_random_number_with_max(maximum):
    return randint(0, maximum - 1)


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


# Function to find modulo inverse of b. It returns
# -1 when inverse doesn't
# modInverse works for prime m
def mod_inverse(b, m):
    g = math.gcd(b, m)
    if (g != 1):
        print("Inverse doesn't exist")
        return -1
    else:
        # If b and m are relatively prime,
        # then modulo inverse is b^(m-2) mode m
        return pow(b, m - 2, m)


# Function to compute a/b under modulo m
def mod_divide(a, b, m):
    a = a % m
    inv = mod_inverse(b, m)
    if (inv == -1):
        print("Division not defined")
    else:
        return (inv * a) % m
