#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, diffrence, multiple and quotient of 5 and 10."""
    from calculator_1 import sum, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))