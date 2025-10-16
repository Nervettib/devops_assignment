from code.calculator import Calculator

def test_add_and_multiply_combination():
    calc = Calculator()
    result = calc.multiply(calc.add(2, 3), 4)
    assert result == 20  # (2 + 3) * 4 = 20

def test_chain_add2_then_multiply2():
    calc = Calculator()
    result = calc.add2_then_multiply2(calc.add(3, 1))  # (3+1)=4 → (4+2)*2=12
    assert result == 12
