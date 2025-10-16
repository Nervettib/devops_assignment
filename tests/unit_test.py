from ..code.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 2) == 8

def test_add2_then_multiply2():
    calc = Calculator()
    assert calc.add2_then_multiply2(3) == 10  # (3 + 2) * 2 = 10
    assert calc.add2_then_multiply2(0) == 4   # (0 + 2) * 2 = 4
    assert calc.add2_then_multiply2(-2) == 0  # (-2 + 2) * 2 = 0
