import math


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(b, a):
    a = int(a)
    b = int(b)
    c = a - b
    return c


def division(b, a):
    a = int(a)
    b = int(b)
    c = a / b
    c = round_half_up(c, 9)
    return c


def round_half_up(n, decimals):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def truncate(n, decimals):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def multiply(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def square(a):
    a = int(a)
    b = a * a
    return b


def sqrt(a):
    a = int(a)
    b = a ** 0.5

    if b < 10:
        b = round_half_up(b, 9)
    else:
        b = round_half_up(b, 8)
    return b


class NLCalculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result
