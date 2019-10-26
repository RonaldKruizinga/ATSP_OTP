from utility import get_random_number


class Sender:
    def __init__(self, g):
        self.m = [0] * 100
        self.g = g

    def init_messages(self):
        for i in range(0, 99):
            self.m[i] = get_random_number()

    def generate_encrypted_messages(self, z0,  z1, x, y):
        if z0 == z1:
            print("no thx")

        r0 = get_random_number()
        s0 = get_random_number()
        r1 = get_random_number()
        s1 = get_random_number()
        w = [0, 0]
        encrypted_m = [0, 0]
        w[0] = x ** s0 * self.g ** r0
        m0_encryption_key = z0 ** s0 * y ** r0
        encrypted_m[0] = self.m[0] ^ m0_encryption_key

        w[1] = x ** s1 * g ** r1
        m1_encryption_key = z1 ** s1 * y ** r1
        encrypted_m[1] = self.m[1] ^ m1_encryption_key
