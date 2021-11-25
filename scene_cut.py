#!/bin/python3

import math
import os
import random
import re
import sys

import ipdb


def _cutTheRest(theRest):
    """Return the lenggth of the first scene in the input"""
    # print(theRest)
    rlen = len(theRest)
    revRest = theRest[::-1]
    index = 0
    i = 0

    while i <= index:
        a = theRest[i]

        rev_index = rlen - 1 - revRest.index(a)

        if rev_index > index:
            # print(index, ' > ', rev_index)
            index = rev_index

        if index == rlen-1:  # corner case when all theRest is one scene
            return rlen

        i += 1

    # print(i, index)
    return index + 1

def cutFilms(inputList):
    res = []
    lleng = l =len(inputList)
    # ipdb.set_trace()
    while l:
        theRest = inputList[lleng-l:]
        scene_len = _cutTheRest(theRest)
        if scene_len:
            res.append(scene_len)
        else:
            break
        l = l - scene_len
    return res


if __name__ == '__main__':
    tests = [
        "ababcbacadefegdehijhklij",
        "abc",
        "abca",
    ]
    for inputstr in tests:
        inputList = [a for a in inputstr]
        result = cutFilms(inputList)
        print(result)
