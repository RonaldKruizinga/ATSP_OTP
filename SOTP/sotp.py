from SOTP.Alice import Alice
from SOTP.Bob import Bob

a = 4  # todo: make dynamic
b = 3  # todo: make dynamic
g = 5  # todo: make dynamic
p = 23  # todo: make dynamic
alice = Alice(g, p, a)
bob = Bob(g, p, b)


def sotp():
    alice.send_secret(bob)
    # todo: hash with SHA1


sotp()
