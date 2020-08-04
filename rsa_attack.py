#!/usr/bin/python3
import time
import math
from rsa_algoritm import generate_keys, encrypt, decrypt
from modular_inverse import modular_inverse


def p_and_q(n):
    """Prime Factorization Algorithm (isn't well for large primes)."""
    c = int(math.sqrt(n)) * 2  # simple reducing number of divisiors
    data = []
    for i in range(2, c):
        if n % i == 0:
            data.append(i)
    return tuple(data)


if __name__ == '__main__':
    # example
    t0 = time.time()
    keysize = 16
    private, public = generate_keys(keysize)
    print("(N, e) = ", public)

    msg = "Hello, RSA!"
    print("Plaintext: " + str(msg))

    en_msg = encrypt(msg, public)
    print("Encrypted msg: " + str(en_msg))

    # ============ Attack ==================

    # Oskar decomposes n into its primes p and q
    data = p_and_q(public[0])
    print(f"Oskar decompose n={public[0]} for p={data[0]}  and q = {data[1]}")

    # Oskar computes phi(n) = (p−1)(q−1)
    phi_N = (data[0] - 1) * (data[1] - 1)

    # Oskar computes d^−1 ≡ e mod Φ(n)
    d, _ = modular_inverse(public[1], phi_N)

    private_key = (public[0], d)
    print("Oskar's private key (N, d) = ", private_key)

    # Oskar decrypted message with x ≡ y^d mod n.
    dr_msg = decrypt(en_msg, private_key)
    print("Oskar decrypted msg: " + str(dr_msg))

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
