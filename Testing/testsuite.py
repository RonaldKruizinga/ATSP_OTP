from SOTP.sotp import sotp
from constants import MESSAGE_COUNT
from pinkas_ot_1n.pinkas1n import pinkas_1n
import time

from utility import get_random_prime, primitive_root


def run_pinkas_1n_iterations(iterations):
    start = time.time()
    print(f"starting {iterations} of pinkas...")

    for i in range(0, iterations):
        pinkas_1n()

    end = time.time()
    return end - start


def run_sotp_1n_iterations(iterations):
    start = time.time()
    print(f"starting {iterations} of pinkas...")

    for i in range(0, iterations):
        sotp()

    end = time.time()
    return end - start


def compare_pinkas_and_sotp(iterations):
    # Calculate primes and generators that will be the same for both protocols
    print("Started generating primes and generators...")
    ps = [0] * iterations
    gs = [0] * iterations
    for i in range(0, iterations):
        p = 0
        while p <= MESSAGE_COUNT:
            p = get_random_prime()
        g = primitive_root(p)
        ps[i] = p
        gs[i] = g
    print("Done generating primes and generators!")
    #
    # 1) Pinkas run
    #
    start = time.time()

    for i in range(0, iterations):
        sotp(ps[i], gs[i])

    end = time.time()
    pinkas_result = end - start
    #
    # 2) SOTP run
    #
    start = time.time()

    for i in range(0, iterations):
        sotp(ps[i], gs[i])

    end = time.time()
    sotp_result = end - start
    # 3) Summarize results
    print("-------------------------")
    print("---------results---------")
    print("-------------------------")
    print(f"pinkas elapsed time: {pinkas_result}s")
    print(f"sotp elapsed time: {sotp_result}s")


compare_pinkas_and_sotp(1000)
