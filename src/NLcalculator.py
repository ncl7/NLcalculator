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
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result
