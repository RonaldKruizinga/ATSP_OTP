from SOTP.Alice import Alice
from SOTP.Bob import Bob
from utility import get_random_number, get_random_prime, primitive_root

a = get_random_number()
b = get_random_number()
p = get_random_prime()
g = primitive_root(p)
print(a, b)
alice = Alice(g, p, a)
bob = Bob(g, p, b)


def sotp():
    alice.send_secret(bob)
    # todo: hash with SHA1


sotp()
