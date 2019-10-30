from SOTP.Alice import Alice
from SOTP.Bob import Bob
from utility import get_random_prime, primitive_root
from ecpy.curves import Curve

# Start the simplest oblivious transfer protocol 1-N based on https://eprint.iacr.org/2015/267.pdf
def sotp():
    # Initialise protocol
    #Algorithm is based on the edwards curve of 2^255-19 (https://en.wikipedia.org/wiki/Ed25519)
    curve = Curve.get_curve("Ed25519")
    p = 2**255-19
    g = curve.order

    print(f"Modulus: {p}, Generator: {g}")

    alice = Alice(g, p)
    bob = Bob(g, p)

    # Start protocol
    alice.send_secret(bob)
    # todo: 1 to n ?
    # todo: g uit curve
    # todo: p = 255-19
    # todo: xor en bitstring?


sotp()
