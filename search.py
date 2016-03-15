#!/usr/bin/env python3

def linear_search(xs, val):
    for i, x in enumerate(xs):
        if x == val:
            return i
    return -1

def binary_search(xs, val):
    lo = 0
    hi = len(xs) - 1
    while lo <= hi:
        i = (lo + hi) // 2
        if xs[i] == val:
            return i
        elif xs[i] > val:
            hi = i - 1
        else:
            lo = i + 1
    return -1


