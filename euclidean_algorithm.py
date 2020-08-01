#!/usr/bin/python3
"""
Greatest Common Divisor (Highest Common Factor) of two numbers:

12 is divided by 1, 2, 3, 4, 6, 12
14 is divided by 1, 2, 7, 14
common diviors are 1, 2.
GDC is 2

===========================

Euclid's algorytm of two numbers: 64, 48.

    (bigger number is on the left)
    a = b * n + a%b

    64 = 48 * n + reminder
    64 = 48 * 1 + 16
    48 = 16 * 3 + 0
    16 = 0 <-- GDC because is 0

"""
import math
import time


def compute_gdc(a, b):
    """Recursive function with Euclid's Algoritm to find gdc."""
    if b == 0:
        return a
    else:
        return compute_gdc(b, a % b)


if __name__ == '__main__':

    # example
    t0 = time.time()

    a = 64
    b = 48

    print(f"GDC of {a} & {b}")
    print(compute_gdc(a, b))

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
