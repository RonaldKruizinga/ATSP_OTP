from utility import get_random_bit, get_random_number


class Chooser:
    def __init__(self):
        pass

    def generate_z(self):
        a = 5
        b = 7
        g = 9
        ga = g ** a
        gb = g ** b
        x = ga
        y = gb
        sigma = get_random_bit()
        print("sigma:" + str(sigma))
        c = [0, 0]
        c[sigma] = a * b
        c[1 - sigma] = get_random_number()
        z0 = g ** c[0]
        z1 = g ** c[1]