from pinkas_ot_1n.message import Message
from constants import MESSAGE_COUNT, DEBUG
from utility import get_random_number_with_max


class Sender:
    m = []  # Messages that chooser is interested in

    def __init__(self, g, p):

        self.g = g  # Group generator
        self.p = p  # Size of group (prime)
        # Init messages if first call
        if not Sender.m:
            Sender.m = [0] * MESSAGE_COUNT
            for i in range(0, MESSAGE_COUNT):
                Sender.m[i] = get_random_number_with_max(self.p)  # Randomly initiate messages
        if DEBUG:
            print(f"messages: {Sender.m}")

    def generate_encrypted_messages(self, label_message):
        x = label_message.x
        y = label_message.y
        z = label_message.z
        w = [0] * MESSAGE_COUNT
        encrypted_m = [0] * MESSAGE_COUNT

        for i in range(0, MESSAGE_COUNT):
            r = get_random_number_with_max(self.p)
            s = get_random_number_with_max(self.p)
            # Encrypt each message with different keys. Only one can be decrypted by chooser, but the sender does not
            # know which one
            w[i] = (x ** s * self.g ** r) % self.p
            m_encryption_key = (z[i] ** s * y ** r) % self.p
            encrypted_m[i] = Sender.m[i] ^ m_encryption_key

        return Message(encrypted_message=encrypted_m, w=w)
