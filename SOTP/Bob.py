import base64
import hashlib

from constants import MESSAGE_COUNT, DEBUG
from utility import get_random_number_with_max


# Temporary encryption function
# In a real life scenario, this should never be used, but to demonstrate the principle of the OTP algorithm
# it will suffice. Real life scenarios should consider algorithms like AES
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


class Bob:
    def __init__(self, generator, modulus):
        self.decryption_key = ""
        self.generator = generator

        # In Zp
        self.secret_bob = get_random_number_with_max(modulus)
        self.modulus = modulus

        self.choice = get_random_number_with_max(MESSAGE_COUNT)  # Randomly choose one of the message values (hardcoded as proof of concept)

        if DEBUG:
            print(f"Bob secret: {self.secret_bob}, choice: {self.choice}")

    def receive_secret_a(self, secret_a, alice):
        if self.choice == 0:
            # g^b % p
            secret_b = pow(self.generator, self.secret_bob, self.modulus)
        else:
            # c*A * g^b % p
            secret_b = self.choice * secret_a * (pow(self.generator, self.secret_bob, self.modulus))
        if DEBUG:
            print(f"Bob encoded secret B: {secret_b}")

        # A^b % p
        decode_key = str(pow(secret_a, self.secret_bob, self.modulus))

        self.decryption_key = hashlib.sha1(decode_key.encode('utf-8')).hexdigest()
        if DEBUG:
            print(f"Bob decryption key: {self.decryption_key}")

        alice.receive_secret_b(secret_b, self)

    def receive_labels(self, encrypted_labels):
        label = decode(self.decryption_key, encrypted_labels[self.choice])
        if DEBUG:
            print(f"Bob result: {label}")
