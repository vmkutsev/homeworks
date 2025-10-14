import pytest

def basketballer(strs):
    baskets = {}
    for word in strs:
        ball = tuple(sorted(word))
        if ball not in baskets:
            baskets[ball] = [word]
        else:
            baskets[ball].append(word)
    return list(baskets.values())

@pytest.mark.parametrize(
    'strs, expected',
    [
        (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
        (['aab', 'aba', 'ab', 'ba'], [['aab', 'aba'], ['ab', 'ba']]),
        (["a", "a", "b", "b"], [["a", "a"], ["b", "b"]])
    ])
def test_basketballer(strs, expected):
    assert basketballer(strs) == expected