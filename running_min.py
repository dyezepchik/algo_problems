#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque


def sliding_min(space, x):
    """
    let i be the inidex of the end of the window
    j - the beginning of the window
    """
    if x == 1:
        return max(space)
    len_sp = len(space)
    if len_sp == 0:
        return None
    if len_sp == 1:
        return space[0]
    if x == len_sp:
        return min(space)
    l = []
    d = deque()
    for i, val in enumerate(space):
        j = i - x + 1
        # if j >= 0:
        #     print(f"Range: {space[j]}:{space[i]}")
        while d and d[-1] > val:
            d.pop()
        
        d.append(val)
        # print(d)
        if j >= 0:
            l.append(d[0])
            # print(f"l = {l}")
            # print(space[j], d[0])
            if space[j] == d[0]:
                d.popleft()
        # print(d)
    return max(l)


def naive_sliding_min(space, x):
    res = [min(space[i-x:i]) for i in range(x, len(space)+1)]
    return max(res)


def test_sliding_min():
    for n in range(10):
        print(f"Test {n}:")
        arr_len = random.randrange(2, 1000)
        win_len = random.randrange(1, arr_len)
        array = [random.randrange(65535) for _ in range(arr_len)]
        expect = naive_sliding_min(array, win_len)
        testing = sliding_min(array, win_len)
        try:
            assert expect == testing
        except:
            print(array)
            print(win_len)
            print(expect, testing)


if __name__ == "__main__":
    # arr = [14, 6, 6, 13, 11, 12]
    # x = 2
    # mins = [1, 2, 3, 3, 4, 2, 2]
    # res = 4
    # print(sliding_min(arr, x))
    # print(naive_sliding_min(arr, x))
    test_sliding_min()