def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def division(a, b):
    return a / b


class NLCalculator:
    result = 0

    def __init__(self):
        x = 1 + 1
        self.result = x
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)

    def subtract(self, a, b):
        self.result = a - b
        return subtraction(a, b)

    def division(self, a, b):
        self.result = a / b
        return division(a, b)

