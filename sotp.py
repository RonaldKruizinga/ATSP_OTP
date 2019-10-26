import hashlib
from random import randint
import base64


def sotp():
    c = randint(0, 1)  # choose between two values
    m0 = "Label0"
    m1 = "label1"
    g = 5  # todo: make dynamic
    p = 23  # todo: make dynamic
    a = 4  # todo: make dynamic
    b = 3  # todo: make dynamic
    A = (g ** a)
    print("A:" + str(A))
    print("c:" + str(c))
    if c == 0:
        B = (g ** b)
    else:
        B = (A * (g ** b))
    print("B:" + str(B))
    #todo: hash with SHA1
    k0 = str(B ** a)
    k1 = str((B / A) ** a)
    kr = str(A ** b)

    e0 = encode(k0, m0)
    e1 = encode(k1, m1)

    if c == 0:
        mc = decode(kr, e0)
    else:
        mc = decode(kr, e1)
    print(mc)
    return False


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


sotp()
