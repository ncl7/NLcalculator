def addition(a, b):
    return a + b


class NLCalculator:
    result = 0

    def __init__(self):
        x = 1 + 1
        self.result = x
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)

