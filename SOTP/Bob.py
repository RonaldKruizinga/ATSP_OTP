import base64

from utility import get_random_bit


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


class Bob:
    def __init__(self, generator, modulus, secret_bob):
        self.decryption_key = ""
        self.generator = generator
        self.secret_bob = secret_bob
        self.modulus = modulus
        self.choice = get_random_bit()  # choose between two values

    def receive_secret_a(self, secret_a, alice):
        if self.choice == 0:
            secret_b = (self.generator ** self.secret_bob) % self.modulus
        else:
            secret_b = secret_a * ((self.generator ** self.secret_bob) % self.modulus)
        self.decryption_key = str((secret_a ** self.secret_bob) % self.modulus)
        alice.receive_secret_b(secret_b, self)

    def receive_labels(self, encrypted_labels):
        label = decode(self.decryption_key, encrypted_labels[self.choice])
        print(label)
