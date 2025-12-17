'''
Идея метода такова, что мы по сути катаем паттерн, который ищем,
по месту, где мы запнулись.
Это позволяет нам не проверять одни и те же символы повторно.
Чтобы понять, на сколько можно откатиться, используем префикс функцию.
Сложность все та же - O(m+n).
'''


import pytest

def kmp_search(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)

    if m == 0:
        return list(range(n + 1))

    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    result = []
    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

def test_classic():
    assert kmp_search("hello world", "world") == [6]


def test_notonly():
    assert kmp_search("abababa", "aba") == [0, 2, 4]


def test_overlap():
    assert kmp_search("aaaaa", "aaa") == [0, 1, 2]


def test_unluck():
    assert kmp_search("abcdef", "gh") == []