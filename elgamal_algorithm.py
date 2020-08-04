#!/usr/bin/python3
import time
import random
from prime_number import is_prime
from euclidean_algorithm import compute_gdc
from modular_inverse import modular_inverse

MIN = pow(10, 5)
MAX = pow(10, 10)


def generate_prime():
    """Generate random prime between MIN and MAX"""
    while True:
        number = random.randint(MIN, MAX)
        if (is_prime(number)):
            return number


def generete_key(p):
    key = random.randint(MIN, p)

    # relatively prime if gcd(p, key) is 1
    while (compute_gdc(p, key) != 1):
        key = random.randint(MIN, p)

    return key


def encrypt(msg, k_m, p):
    en_msg = []

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    for i in range(0, len(en_msg)):
        en_msg[i] = (k_m * ord(en_msg[i])) % p

    return en_msg


def decrypt(en_msg, k_m, p):
    dr_msg = []
    # a^-1 = x (mod m)
    # a.x = 1 (mod m), therefore
    # k_m.x = 1 (mod p)
    k_m_inv, _ = modular_inverse(k_m, p)
    print(f"Multiplicative Modular Inverse of Km: {k_m_inv}")

    for i in range(0, len(en_msg)):
        dr_msg.append(chr(en_msg[i] * k_m_inv % p))

    return "".join(dr_msg)


if __name__ == '__main__':

    t0 = time.time()
    # 1. Bob chooses large prime p
    p = generate_prime()
    print(f"Public prime is {p}")

    # 2. Bob chooses primitive element α ∈ Z*p
    alpha = random.randint(2, 10)
    print(f"Primitive Element {alpha}")

    # 3. Bob chooses k_pr = d ∈ {2, ... , p−2}
    k_pr = d = generete_key(p - 2)

    # 4. Bob computes k_pub = β = α ^ d mod p
    beta = pow(alpha, d, p)
    k_pub = (p, alpha, beta)

    print(f"Public key is {k_pub}")

    # 5. Alice chooses i ∈ {2, ... , p−2}
    i = generete_key(p - 2)

    # 6. Alice computes ephemeral key
    k_e = pow(k_pub[1], i, k_pub[0])
    print(f"Ephemeral key is {k_e}")

    # 7. Alice computes masking key
    k_m = pow(k_pub[2], i, k_pub[0])

    # 8. Alice encrypt message x ∈ Z∗p
    x = "Hello, ElGamal!"
    print(f"Messeage is: {x}")

    en_msg = encrypt(x, k_m, k_pub[0])
    print(f"Encrypt message {en_msg}")

    # 9. Bob computes masking key
    k_m_ = pow(k_e, d, p)
    dr_msg = decrypt(en_msg, k_m_, p)
    print(f"Decrypt message: {dr_msg}")

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
