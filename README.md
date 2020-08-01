# Python Algoritms

## Prime Number test

Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.

## Generating large random primes

https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb

## Euclidean Algorithm

The Euclidean algorithm is correct, i.e., it returns the greatest common
divisor of two given positive integers.

## Extended Euclidean Algorithm

The extended Euclidean algorithm returns the greatest common divisor of two
given numbers, and, moreover, it determines the integer coefficients s and t of a
linear combination such that gcd(n,m) = s.n + t.m.

## Modular Inverse

Given two integers ‘a’ and ‘m’, find modular multiplicative inverse of ‘a’ under modulo ‘m’.

The modular multiplicative inverse is an integer ‘x’ such that.

a · x ≡ 1 (mod m)

The value of x should be in {0, 1, 2, … m-1}, i.e., in the range of integer modulo m.

The multiplicative inverse of `a modulo m` exists if and only if a and m are relatively prime (i.e., if gcd(a, m) = 1).

## RSA Algoritm

The algorithm enables encryption and decryption with the use of a pair of keys:
a public and a private one, according to the idea of asymmetric cryptography. RSA
is a cryptosystem that also allows encryption of messages with a private key and, in
such a case, to decrypt them with a public key (used for digital signatures).

1. Choose two large random primes p and q.
2. Choose a random integer e such that 1 < e < (p − 1) · (q − 1) and
   GCD((p −1) · (q − 1), e) = 1.
3. Find an integer d that is the inverse of e modulo (p − 1) · (q − 1) (if such
   an inverse does not exist, then choose another e), i.e., such that e · d = 1mod(p −1) · (q −1).
4. Compute n = p · q (at this moment it is recommended to delete p and q in order
   to prevent them from being obtained by an eavesdropper).
5. Your public key is (e, n) and the private key is (d, n).

## Diffie-Hellman Algorithm

The basic idea behind the DHKE is that exponentiation in Z∗p,
p prime, is a one-way function and that exponentiation is commutative, i.e.,

k = (α^x)·y ≡ (α^y)·x mod p
