import base64
import hashlib
from utility import get_random_number


# Temporary encryption function
# In a real life scenario, this should never be used, but to demonstrate the principle of the OTP algorithm
# it will suffice. Real life scenarios should consider algorithms like AES
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


class Alice:
    # Simple labels for easy understanding. Should be longer and random string in a real application.
    messages = ["label0", "label1"]

    def __init__(self, generator, modulus):
        self.generator = generator

        # Between 1 and 10000
        self.secret_alice = get_random_number()
        self.modulus = modulus

        # g^a % p = A
        self.encoded_secret = (self.generator ** self.secret_alice) % self.modulus
        print(f"Alice secret: {self.secret_alice}, encoded: {self.encoded_secret}")

    def send_secret(self, bob):
        bob.receive_secret_a(self.encoded_secret, self)

    def receive_secret_b(self, secret_b, bob):
        # k_0 = B^a % p
        key_0 = str((secret_b ** self.secret_alice) % self.modulus)
        hashed_key_0 = hashlib.sha1(key_0.encode('utf-8')).hexdigest()

        # k_1 = (B/A)^a % p
        key_1 = str((int(secret_b / self.encoded_secret) ** self.secret_alice) % self.modulus)
        hashed_key_1 = hashlib.sha1(key_1.encode('utf-8')).hexdigest()

        print(f"Alice keys: {hashed_key_0}, {hashed_key_1}")

        encrypted_0 = encode(hashed_key_0, self.messages[0])
        encrypted_1 = encode(hashed_key_1, self.messages[1])

        print(f"Alice encrypted: {encrypted_0}, {encrypted_1}")

        bob.receive_labels([encrypted_0, encrypted_1])

