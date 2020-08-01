#!/usr/bin/python3
"""
DHKE consists of two protocols, the set-up protocol and the main protocol,
which performs the actual key exchange.

"""
import time
import random
from prime_number import is_prime


def generate_prime(keysize):
    """
    :return: random large prime number of keysize bits in size
    """
    while True:
        number = random.randrange(2 ** (keysize - 1), (2 ** keysize) - 1)
        if (is_prime(number)):
            return number


if __name__ == '__main__':

    t0 = time.time()

    # 1.1 Choose a large prime p.
    p = generate_prime(keysize=32)

    # 1.2 Choose an integer α ∈ {2,3, . . . , p−2}.
    alpha = random.randint(2, p)

    # 1.3 Publish p and α.
    print(f"p = {p}")
    print(f"α = {alpha}")

    # 2.1 Alice chooses a large integer `a` randomly and computes A = a ^ alpha mod p.
    a = random.randint(2, p - 1)    # private key A
    # Modular exponentiation
    A = pow(alpha, a, p)             # public key A

    # 2.1 Alice sends the value A to Bob.
    print(f"Alice's public key is {A}")

    # 3.1 Bob chooses a large integer `b` randomly and computes B = b ^ alpha mod p.
    b = random.randint(2, p - 1)    # private key A
    # Modular exponentiation
    B = pow(alpha, b, p)             # public key A

    # 3.1 Bob sends the value B to Alice.
    print(f"Bobs's public key is {B}")

    # 4.1 Alice computes ka = B ^ a mod p
    ka = pow(B, a, p)  # Secret key for Alice

    # 4.2 Bob computes kb = A ^ b mod p
    kb = pow(A, b, p)  # // Secret key for Bob

    print(f"Secret key for the Alice is : {ka}")
    print(f"Secret Key for the Bob is : {kb}")

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
