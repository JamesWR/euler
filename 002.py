"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""
import util


def main():
    total = 0
    i = 2
    curfeb = util.feb(i)
    while curfeb <= 4000000:
        total += curfeb
        i += 3
        curfeb = util.feb(i)
    print(total)


if __name__ == "__main__":
    main()

