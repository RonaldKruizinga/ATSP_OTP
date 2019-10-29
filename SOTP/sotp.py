from SOTP.Alice import Alice
from SOTP.Bob import Bob
from utility import get_random_prime, primitive_root


# Start the simplest oblivious transfer protocol
def sotp():
    # Initialise protocol

    p = get_random_prime()
    g = primitive_root(p)

    print(f"Modulus: {p}, Generator: {g}")

    alice = Alice(g, p)
    bob = Bob(g, p)

    # Start protocol
    alice.send_secret(bob)
    # todo: hash with SHA1
    # todo: implement actual encryption
    # todo: 1 to n ?


sotp()
