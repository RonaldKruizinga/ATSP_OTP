from pinkas_ot.chooser import Chooser
from pinkas_ot.sender import Sender
from utility import get_random_prime, primitive_root


def run_pinkas():
    p = get_random_prime()
    g = primitive_root(p)
    #p = 397
    #g = 5
    print(p, g)
    sender = Sender(g, p)
    chooser = Chooser(g, p)

    label_message = chooser.generate_labels()
    encrypted_result_message = sender.generate_encrypted_messages(label_message)
    result = chooser.decrypt_message(encrypted_result_message)
    print(result)
#
# def pinkas():
#     m = [45, 57]
#     # --------
#     # Chooser:
#     # --------
#     a = 5
#     b = 7
#     g = 9
#     ga = g ** a
#     gb = g ** b
#     x = ga
#     y = gb
#     sigma = get_random_bit()
#     print("sigma:" + str(sigma))
#     c = [0, 0]
#     c[sigma] = a * b
#     c[1-sigma] = get_random_number()
#     z0 = g ** c[0]
#     z1 = g ** c[1]
#     # -------
#     # Sender:
#     # -------
#     # Validate z0 != z1
#     if z0 == z1:
#         print("no thx")
#
#     r0 = get_random_number()
#     s0 = get_random_number()
#     r1 = get_random_number()
#     s1 = get_random_number()
#     w = [0, 0]
#     encrypted_m = [0, 0]
#     w[0] = x ** s0 * g ** r0
#     m0_encryption_key = z0 ** s0 * y ** r0
#     encrypted_m[0] = m[0] ^ m0_encryption_key
#
#     w[1] = x ** s1 * g ** r1
#     m1_encryption_key = z1 ** s1 * y ** r1
#     encrypted_m[1] = m[1] ^ m1_encryption_key
#
#     # --------
#     # Chooser:
#     # --------
#     print((w[sigma]**b) ^ encrypted_m[sigma])


run_pinkas()
