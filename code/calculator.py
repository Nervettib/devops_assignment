class Calculator:

    def add(self, a, b):
        c = 'XY'
        return a + b

    def multiply(self, a, b):
        return a * b

    def add2_then_multiply2(self, x):
        return self.multiply( self.add(x, 2), 2)