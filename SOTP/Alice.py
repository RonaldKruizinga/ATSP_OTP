import base64
import hashlib
from utility import get_random_number_with_max


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
    # Simple labels for easy understanding. Should be longer and random string in a real application. Hardcoded as proof of concept
    messages = ["label0", "label1", "label2", "label3", "label4", "label5", "label6", "label7", "label8", "label9"]

    def __init__(self, generator, modulus):
        self.generator = generator

        # in Zp
        self.secret_alice = get_random_number_with_max(modulus)
        self.modulus = modulus

        # g^a % p = A
        self.encoded_secret = (self.generator ** self.secret_alice) % self.modulus
        print(f"Alice secret: {self.secret_alice}, encoded: {self.encoded_secret}")

    def send_secret(self, bob):
        bob.receive_secret_a(self.encoded_secret, self)

    def receive_secret_b(self, secret_b, bob):
        keys_and_labels = [(str((int(secret_b / (self.encoded_secret * c)) ** self.secret_alice) % self.modulus), self.messages[c]) for c in range(1, 10)]
        keys_and_labels.insert(0, (str((secret_b ** self.secret_alice) % self.modulus), self.messages[0])) # Special case for label 0 as the list comprehension above would divide by zero when we use it
        encoded_messages = [encode(hashlib.sha1(key.encode('utf-8')).hexdigest(), label) for key, label in keys_and_labels]
        print(f"Alice encrypted: {encoded_messages}")

        bob.receive_labels(encoded_messages)
