from Test_Programs import mathop


def test_add():
    total = mathop.add(4, 5)
    assert total == 9


def test_mul():
    total = mathop.mul(4, 5)
    assert total == 20


def test_sub():
    total = mathop.sub(7, 5)
    assert total == -2
