#!/usr/bin/python3
"""
Multiplicative Inverse of `a` under modulo `m`.
a * x ≡ 1 (mod m)

The value of x should be in {0, 1, 2, … m-1}

The multiplicative inverse of `a modulo m` exists 
if and only if a and m are relatively prime (i.e., if gcd(a, m) = 1).

e.g
m = 7, a = 4, x = 2     4 * 2 = 8 mod 7 = 1
m = 11, a = 8, x = 7    87 = 56 mod 11 = 1

"""
import time
from extended_euclidean_algorithm import gcd_extended


def modular_inverse(a, m):
    """Based on Extended Euler’s GCD algorithm [Works when a and m are coprime]"""
    gdc, x, _ = gcd_extended(a, m)
    if gdc != 1:
        raise Exception("Inverse doesn't exists")
    else:
        res = (x % m + m) % m
        return res, x


if __name__ == '__main__':
    # example
    t0 = time.time()

    a = 16
    m = 29

    mod_inv, x = modular_inverse(a, m)
    print(f"{a} * {x} mod {m} = {mod_inv}")

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
