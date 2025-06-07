import math
import sys

try:
    sys.set_int_max_str_digits(0)
except AttributeError:
    pass


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(limit: int):
    """Generate all primes <= limit using a simple sieve."""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:limit + 1:step] = [False] * len(sieve[start:limit + 1:step])
    for num, isprime in enumerate(sieve):
        if isprime:
            yield num


def product_of_primes(limit: int) -> int:
    """Return the product of all primes up to limit."""
    result = 1
    for p in primes_up_to(limit):
        result *= p
    return result


if __name__ == "__main__":
    LIMIT = 100_000
    prod = product_of_primes(LIMIT)
    print(prod)
