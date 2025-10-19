import main
import math
import pytest

@pytest.mark.basic
def test_main_1():
    numbers = [10, 5, 20, 0, 40, 45, 50, 55, 9, 10]
    ret = main.getFarNumber(numbers)
    print(f'Your return value is {ret}')
    assert ret == 55, f'Expected 55 but got {ret}'

@pytest.mark.edge
def test_main_2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
    ret = main.getFarNumber(numbers)
    print(f'Your return value is {ret}')
    assert ret == 20, f'Expected 20 but got {ret}'

@pytest.mark.bonus
def test_main_3():
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 500]
    ret = main.getFarNumber(numbers)
    print(f'Your return value is {ret}')
    assert ret == 500, f'Expected 500 but got {ret}'

@pytest.mark.bonus
def test_main_4():
    numbers = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    ret = main.getFarNumber(numbers)
    print(f'Your return value is {ret}')
    assert ret == 10, f'Expected 10 but got {ret}'