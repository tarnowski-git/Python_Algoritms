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

![obraz](https://user-images.githubusercontent.com/34337622/89286425-782b7e00-d652-11ea-9858-ed285b80dd7d.png)

## Diffie-Hellman Algorithm

The basic idea behind the DHKE is that exponentiation in Z∗p,
p prime, is a one-way function and that exponentiation is commutative, i.e.,

k = (α^x)·y ≡ (α^y)·x mod p

![obraz](https://user-images.githubusercontent.com/34337622/89286347-53cfa180-d652-11ea-9840-5dcacc32a94f.png)

## El Gamal Algorithm

![obraz](https://user-images.githubusercontent.com/34337622/89286190-0d7a4280-d652-11ea-8b50-b544df8bcccb.png)

## RSA Mathematical Attacks

0. Decompose n into its primes p and q.
1. Φ(n) = (p−1)(q−1)
2. d^−1 ≡ e mod Φ(n)
3. x ≡ y^d mod n.

![obraz](https://user-images.githubusercontent.com/34337622/89356083-35eb5680-d6bd-11ea-95a7-4a307379dd1a.png)
