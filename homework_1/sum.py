import pytest

def suma_maxima(lista):
    lista = [int(x) for x in lista.split()]
    odda = []
    suma = 0
    for x in lista:
        if x % 2 == 0:
            suma += x
        else:
            odda.append(x)
    if len(odda) % 2 != 0:
        odda.sort()
        odda.remove(odda[0])
    suma += sum(odda)
    return(suma)

@pytest.mark.parametrize("s, expected", [
    ('1', 0), # единственное нечётное → пустое подмножество: 0
    ('2', 2), # единственное чётное → берём его
    ('1 2 3', 6), # сумма всех (6) уже чётная
    ('2 5 6', 8), # 2+5+6=13 (нечёт), выкидываем мин. нечётное 5 → 8
    ('1 3 5', 8), # 1+3+5=9, выкидываем 1 → 8
    ('2 4 6', 12), # все чётные → берём все
    ('9 9', 18), # 9+9=18
    ('7 7 7', 14), # 7+7+7=21, выкидываем 7 → 14
    ('10 1', 10), # 11 нечёт, выкидываем 1 → 10
    ('1000001 1000001', 2000002),
    ('1 1 1 2 2 1 3', 10) # много чисел
])
def test_suma_maxima(s, expected):
    assert suma_maxima(s) == expected

