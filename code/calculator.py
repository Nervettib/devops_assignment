class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def add2_then_multiply2(self, x):
        return Calculator.multiply( Calculator.add(x, 2), 2)