from pinkas_ot.chooser import Chooser
from pinkas_ot.sender import Sender
from utility import get_random_prime, primitive_root


def pinkas():
    p = get_random_prime()
    g = primitive_root(p)

    print(f"p:{p}, g:{g}")
    sender = Sender(g, p)
    chooser = Chooser(g, p)

    label_message = chooser.generate_labels()
    encrypted_result_message = sender.generate_encrypted_messages(label_message)
    result = chooser.decrypt_message(encrypted_result_message)
    print(result)

