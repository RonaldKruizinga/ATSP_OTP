from pinkas_ot.message import Message
from utility import get_random_bit, get_random_number


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
        self.a = get_random_number()
        self.b = get_random_number()

    def generate_labels(self):

        ga = (self.g ** self.a) % self.p
        gb = (self.g ** self.b) % self.p
        x = ga
        y = gb
        # Randomly choose if want the label for 0 or 1
        self.sigma = get_random_bit()
        print("sigma:" + str(self.sigma))
        # The c of sigma is build using a and b. The other is random.
        c = [0, 0]
        c[self.sigma] = self.a * self.b
        c[1 - self.sigma] = get_random_number()
        z0 = (self.g ** c[0]) % self.p
        z1 = (self.g ** c[1]) % self.p
        return Message(x=x, y=y, z0=z0, z1=z1)

    def decrypt_message(self, message):
        # Decrypt using XOR to find results
        return ((message.w[self.sigma] ** self.b) % self.p) ^ message.encrypted_message[self.sigma]
