import pytest

def matcher(arr, k):
    olds = {}
    for i, x in enumerate(arr):
        if k - x in olds:
            return olds[k - x], i
        olds[x] = i

@pytest.mark.parametrize(
    'arr, k, expected',
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([10, -2, 4, 6], 4, (1, 3)),
        ([0, 0, 3, 4], 0, (0, 1))
    ]
)
def test_matcher(arr, k, expected):
    assert matcher(arr, k) == expected
