from pinkas_ot.message import Message
from utility import get_random_bit, get_random_number


class Chooser:
    sigma = 0  # just a default value, will be set in init
    b = 0
    a = 0
    g = 0
    p = 0

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
        self.sigma = get_random_bit()
        print("sigma:" + str(self.sigma))
        c = [0, 0]
        c[self.sigma] = self.a * self.b
        c[1 - self.sigma] = get_random_number()
        z0 = (self.g ** c[0]) % self.p
        z1 = (self.g ** c[1]) % self.p
        return Message(x=x, y=y, z0=z0, z1=z1)

    def decrypt_message(self, message):
        return ((message.w[self.sigma] ** self.b) % self.p) ^ message.encrypted_message[self.sigma]
