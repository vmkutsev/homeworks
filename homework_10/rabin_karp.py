"""
Наша хеш-функция выглядит так:
     H(s[0..m-1]) =
            s[0] * base^(m-1) +
            s[1] * base^(m-2) +
            ...
            s[m-1]
Вычисления делаем по модулю, при сдвиге удаляем вклад уходящего,
добавляем вклад приходящего. Выглядит это так:
    H_new =
        (H_old - left_char * base^(m-1)) * base + right_char

Что касается сложности, то в среднем она у нас O(n+m),
по памяти обновляемся за O(1). Такие дела
"""
import pytest

def rabin_karp(text: str, pattern: str) -> list[int]:
    n, m = len(text), len(pattern)
    base = 256
    mod = 10 ** 9 + 7

    high_power = pow(base, m - 1, mod)

    pattern_hash = 0
    window_hash = 0

    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    result = []

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * high_power) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod

    return result

def test_classic():
    assert rabin_karp("hello world", "world") == [6]


def test_notonly():
    assert rabin_karp("abababa", "aba") == [0, 2, 4]


def test_overlap():
    assert rabin_karp("aaaaa", "aaa") == [0, 1, 2]


def test_unluck():
    assert rabin_karp("abcdef", "gh") == []