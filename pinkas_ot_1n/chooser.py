from pinkas_ot_1n.message import Message
from pinkas_ot_1n.constants import MESSAGE_COUNT
from utility import get_random_number_with_max


class Chooser:
    # Just a default values; will be set in init
    sigma = 0  # Interested message index
    b = 0  # Random number
    a = 0  # Random number
    g = 0  # Generator of G
    p = 0  # Prime; size of cyclic group G

    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.a = get_random_number_with_max(p)
        self.b = get_random_number_with_max(p)

    def generate_labels(self):

        ga = pow(self.g, self.a, self.p)
        gb = pow(self.g, self.b, self.p)
        x = ga
        y = gb
        # Randomly choose which message we are interested in
        self.sigma = get_random_number_with_max(MESSAGE_COUNT-1)
        print(f"sigma:{self.sigma}")
        # The c of sigma is build using a and b. The others are random members of G

        z = [0] * MESSAGE_COUNT
        c_sigma = self.a * self.b
        # z_sigma is calculated normally, based on c_sigma and thus on a and b.
        z[self.sigma] = pow(self.g, c_sigma, self.p)

        # The other z's are random members of G
        for j in range(0, MESSAGE_COUNT):
            if j == self.sigma:
                # Already calculated; skip
                pass
            else:
                z[j] = (z[self.sigma] * (self.g ** self.get_cycle_index(j - self.sigma))) % self.p

        return Message(x=x, y=y, z=z)

    def decrypt_message(self, message):
        # w[sigma] is actually g^(s*a+r)
        # The used encryption key is g^(s*a*b+r*b) thus we need to raise w to the power b
        # After this, decrypt using XOR to find results
        return pow(message.w[self.sigma], self.b, self.p) ^ message.encrypted_message[self.sigma]

    # Map negative indices "-i" in the group to "p-1-i"
    def get_cycle_index(self, i):
        if i > 0:
            return i
        else:
            return self.p - 1 - i
