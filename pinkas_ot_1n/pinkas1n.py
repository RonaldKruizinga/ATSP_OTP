from pinkas_ot_1n.chooser import Chooser
from constants import MESSAGE_COUNT, DEBUG
from pinkas_ot_1n.sender import Sender
from utility import get_random_prime, primitive_root


def pinkas_1n(p=None, g=None):
    # p should be greater than message count, to account for calculations of g ** message_index
    # as p is the size of group G
    if not p:
        while p <= MESSAGE_COUNT:
            p = get_random_prime()
    # generator of cyclic group G of size p
    if not g:
        g = primitive_root(p)
    if DEBUG:
        print(f"p:{p}, g:{g}")
    sender = Sender(g, p)
    chooser = Chooser(g, p)

    label_message = chooser.generate_labels()
    encrypted_result_message = sender.generate_encrypted_messages(label_message)
    result = chooser.decrypt_message(encrypted_result_message)
    print(result)
