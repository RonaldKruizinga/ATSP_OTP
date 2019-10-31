from SOTP.Alice import Alice
from SOTP.Bob import Bob
from constants import DEBUG
from utility import get_random_prime, primitive_root


# Start the simplest oblivious transfer protocol as a 1-N protocol based on Diffie-Hellman (implemented as 1-10 as proof of concept)
def sotp(p=None, g=None):
    # Initialise protocol
    if not p:
        p = get_random_prime()
    if not g:
        g = primitive_root(p)
    if DEBUG:
        print(f"Modulus: {p}, Generator: {g}")

    alice = Alice(g, p)
    bob = Bob(g, p)

    # Start protocol
    alice.send_secret(bob)
