import base64


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.decode()


class Alice:
    messages = ["label0", "label1"]

    def __init__(self, generator, modulus, secret_alice):
        self.generator = generator
        self.secret_alice = secret_alice
        self.modulus = modulus
        self.encoded_secret = (self.generator ** self.secret_alice) % self.modulus

    def send_secret(self, bob):
        bob.receive_secret_a(self.encoded_secret, self)

    def receive_secret_b(self, secret_b, bob):
        key_0 = str((secret_b ** self.secret_alice) % self.modulus)
        key_1 = str((int(secret_b / self.encoded_secret) ** self.secret_alice) % self.modulus)
        encrypted_0 = encode(key_0, self.messages[0])
        encrypted_1 = encode(key_1, self.messages[1])
        bob.receive_labels([encrypted_0, encrypted_1])

