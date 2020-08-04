#!/usr/bin/python3
"""
The extended Euclidean algorithm updates results of gcd(a, b) 
using the results calculated by recursive call gcd(b % a, a).
    gcd(a, b) = a.x + b.y

And x1 and y1 are results for inputs b%a and a
   (b%a).x1 + a.y1 = gcd

When we put b%a = (b - (⌊b/a⌋).a) in above, 
we get following. Note that ⌊b/a⌋ is floor(b/a)

   (b - (⌊b/a⌋).a).x1 + a.y1  = gcd

Above equation can also be written as below
   b.x1 + a.(y1 - (⌊b/a⌋).x1) = gcd      ---(2)

After comparing coefficients of 'a' and 'b' in (1) and 
(2), we get following
   x = y1 - ⌊b/a⌋ * x1
   y = x1
"""
import time


def gcd_extended(a, b):
    # Base Case
    # gdc(a, b) = 0 * x + 1 *y
    if a == 0:
        x, y = 0, 1
        # b is a GDC
        return b, x, y

    gcd, x1, y1 = gcd_extended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


if __name__ == '__main__':

    # example
    t0 = time.time()

    a, b = 16, 13
    gdc, x, y = gcd_extended(a, b)
    print(f"gcd({a}, {b}) = {a} * {x} + {b} * {y} = {gdc}")

    t1 = time.time()
    print("Time reqired: ", t1 - t0)
