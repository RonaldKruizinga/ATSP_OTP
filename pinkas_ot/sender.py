from pinkas_ot.message import Message
from utility import get_random_number


class Sender:
    g = 0
    m = []
    p = 0

    def __init__(self, g, p):
        self.m = [0] * 100
        self.g = g
        self.p = p
        for i in range(0, 99):
            self.m[i] = get_random_number()

        print("m[0]:" + str(self.m[0]))
        print("m[1]:" + str(self.m[1]))

    def generate_encrypted_messages(self, label_message):
        x = label_message.x
        y = label_message.y
        z0 = label_message.z0
        z1 = label_message.z1

        if z0 == z1:
            print("no thx")

        r0 = get_random_number()
        s0 = get_random_number()
        r1 = get_random_number()
        s1 = get_random_number()
        w = [0, 0]
        encrypted_m = [0, 0]
        w[0] = (x ** s0 * self.g ** r0) % self.p
        m0_encryption_key = (z0 ** s0 * y ** r0) % self.p
        encrypted_m[0] = self.m[0] ^ m0_encryption_key

        w[1] = (x ** s1 * self.g ** r1) % self.p
        m1_encryption_key = (z1 ** s1 * y ** r1) % self.p
        encrypted_m[1] = self.m[1] ^ m1_encryption_key

        return Message(encrypted_message=encrypted_m, w=w)
