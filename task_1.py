import timeit
from random import randint


def isEvenBitsAND(number):
    """
    Bitwise AND number with 1.

    number: int
    return: bool
    """
    return number & 1 == 0


def isEvenBitsSHIFT(number):
    """
    Apply a bitwise shift to the number. First to the right by one, then to the left by one.
    Compare the result with a number.

    number: int
    return: bool
    """
    x = number >> 1
    return x << 1 == number


def isEvenExample(number):
    """
    The remainder of division by 2 is compared to zero.

    number: int
    return: bool
    """
    return number % 2 == 0


if __name__ == "__main__":
    firstTestGenerator = iter(range(5000000))
    secondTestGenerator = iter(range(5000000))
    thirdTestGenerator = iter(range(5000000))

    print(
        timeit.timeit(
            "isEvenBitsAND(next(firstTestGenerator))",
            "from __main__ import isEvenBitsAND, firstTestGenerator",
            number=5000000))
    print(
        timeit.timeit(
            stmt="isEvenBitsSHIFT(next(secondTestGenerator))",
            setup="from __main__ import isEvenBitsSHIFT, secondTestGenerator",
            number=5000000
        ))
    print(
        timeit.timeit(
            "isEvenExample(next(thirdTestGenerator))",
            "from __main__ import isEvenExample, thirdTestGenerator",
            number=5000000))
