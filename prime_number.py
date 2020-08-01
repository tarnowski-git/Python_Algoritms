#!/usr/bin/python3
import math
import time


def is_prime(n):
    """Return `True` if `n` is a prime number. `False` otherwise."""

    # Corner case
    if (n <= 1):
        return False

    # Carring that 2 and 3 is prime !
    if (n > 2 and n % 2 == 0):
        return False

    # Reducing number of divisiors we check
    #  n = 1 * n
    #    = a * b
    #    = ...
    #    = sqrt(n) * sqrt(n)
    #    = ...
    #    = b * a
    #    = n * 1
    max_divisior = math.floor(math.sqrt(n))

    # testing only odd divisors
    for d in range(3, 1 + max_divisior, 2):
        if n % d == 0:
            return False

    return True


if __name__ == '__main__':

    # example
    t0 = time.time()

    for i in range(0, 1000):
        print(i)

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
