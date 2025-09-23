import pytest

def is_palindromus(numberus):
    numberus = int(numberus)
    digs = 0 # поймем сколько цифр в числе
    while numberus // 10**digs != 0:
        digs += 1
    for i in range(1, digs//2+1): # если цифр нечетное кол-во, проверять среднюю не будем
        left = numberus // 10**(digs-i) - numberus // 10**(digs-i+1) * 10
        right = numberus // 10**(i-1) % 10
        if right != left: # как только цифра справа не совпадет с цифрой слева, цикл сломается
            return False
    return True

@pytest.mark.parametrize('n', [
    1, 2, 7, 9, # одноцифровые
    11, 22, 3883, # чётные длины
    101, 121, 32123, # нечётные длины
    1001, 120021, 1000001, 1234321
])
def test_palindromus(n):
    assert is_palindromus(n) is True

@pytest.mark.parametrize('n', [
    12, 10, 123, 1231, 2001, 100, 110, 1002, 123456, 112233, 120012
])
def test_non_palindromus(n):
    assert is_palindromus(n) is False