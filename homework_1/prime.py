import pytest

def primer(numer):
    numer = int(numer)
    pr_list = []
    for num in range(2,numer):
        checker = True
        for prim in pr_list:
            if num % prim == 0:
                checker = False
        if checker == True:
            pr_list.append(num)
    return len(pr_list)

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 1), # {2}
    (4, 2), # {2, 3}
    (5, 2), # {2, 3}
    (10, 4), # {2, 3, 5, 7}
    (11, 4), # 11 не считается
    (12, 5), # добавится 11
    (100, 25), # нагуглил
    (1000, 168), # тоже
])
def test_primer(n, expected):
    assert primer(n) == expected