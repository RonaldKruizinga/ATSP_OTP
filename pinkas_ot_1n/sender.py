from pinkas_ot_1n.message import Message
from pinkas_ot_1n.constants import MESSAGE_COUNT
from utility import get_random_number_with_max


class Sender:
    g = 0
    m = []
    p = 0

    def __init__(self, g, p):
        self.m = [0] * MESSAGE_COUNT
        self.g = g
        self.p = p
        for i in range(0, MESSAGE_COUNT):
            self.m[i] = get_random_number_with_max(self.p)

        print(self.m)

    def generate_encrypted_messages(self, label_message):
        x = label_message.x
        y = label_message.y
        z = label_message.z
        w = [0] * MESSAGE_COUNT
        encrypted_m = [0] * MESSAGE_COUNT

        for i in range(0, MESSAGE_COUNT):
            r = get_random_number_with_max(self.p)
            s = get_random_number_with_max(self.p)

            w[i] = (x ** s * self.g ** r) % self.p
            m_encryption_key = (z[i] ** s * y ** r) % self.p
            encrypted_m[i] = self.m[i] ^ m_encryption_key

        return Message(encrypted_message=encrypted_m, w=w)
