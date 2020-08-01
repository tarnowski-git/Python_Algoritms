#!/usr/bin/python3
import time
# required for the sqrt() function, if you want to avoid doing **0.5
from math import sqrt
import random
from prime_number import is_prime
from euclidean_algorithm import compute_gdc
from modular_inverse import modular_inverse

# https://www.youtube.com/watch?v=shaQZg8bqUM&t=47s


def generate_prime(keysize):
    """
    :return: random large prime number of keysize bits in size
    """
    while True:
        number = random.randrange(2 ** (keysize - 1), (2 ** keysize) - 1)
        if (is_prime(number)):
            return number


def encrypt(msg_plaintext, package):
    # unpack key value pair
    N, e = package
    msg_ciphertext = []
    for c in msg_plaintext:
        # For example, ord(‘a’) returns the integer 97, ord(‘€’) (Euro sign) returns 8364
        m = ord(c)
        # pow(base, exp[, mod])
        msg_ciphertext.append(pow(m, e, N))

    return msg_ciphertext


def decrypt(msg_ciphertext, package):
    N, d = package
    msg_plaintext = ""
    for part in msg_ciphertext:
        if part:
            c = int(part)
            msg_plaintext += chr(pow(c, d, N))

    return msg_plaintext


def generate_keys(keysize=32):

    # 1. choose two (large) primes p and q

    p = generate_prime(keysize)
    q = generate_prime(keysize)

    # 2. compute n = p · q
    # RSA Modulus
    N = p * q

    # 3. compute phi(n) = (p−1)(q−1)
    # totient
    phi_N = (p - 1) * (q - 1)

    # 4. Select the public exponent e in {1,2, . . . ,phi(n)−1} such that gcd(e,phi(n)) == 1.
    # e is coprime with phi_N & 1 < e <= phiN
    while True:
        e = random.randrange(2 ** (keysize - 1), (2 ** keysize) - 1)
        # relatively prime if gcd(p, q) is 1
        if compute_gdc(e, phi_N) == 1:
            break

    # 5. Compute the private key d such that d.e ≡ 1 (mod phi(n))
    d, _ = modular_inverse(e, phi_N)

    key_public = (N, e)
    print("Public Key: ", key_public)

    key_private = (N, d)
    print("Private Key: ", key_private)

    return (key_private, key_public)


if __name__ == '__main__':

    t0 = time.time()

    print("Running RSA...")
    keysize = 32
    private, public = generate_keys(keysize)

    x = "Hello, RSA!"
    print("Plaintext: " + str(x))

    y = encrypt(x, public)
    print("Encrypted msg: " + str(y))

    x = decrypt(y, private)
    print("Decrypted msg: " + str(x))

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
