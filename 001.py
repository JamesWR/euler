"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import math


def main():
    n = math.floor(999 / 3)
    threes = 3 * (n + 1) * n / 2
    n = math.floor(999 / 5)
    fives = 5 * (n + 1) * n / 2
    n = math.floor(999 / 15)
    fifteens = 15 * (n + 1) * n / 2
    print(int(threes + fives - fifteens))


if __name__ == "__main__":
    main()

