#!/usr/bin/env python3
"""
Boloutare Doubeni 2016
"""


def default_cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def __merge(xs, lo, mid, hi, compare=default_cmp):
    i = lo
    j = mid + 1
    aux = xs

    for k in range(lo, hi+1):
        if k > mid:
            j += 1
            xs[k] = aux[j]
        elif j > hi:
            i += 1
            xs[k] = aux[i]
        elif compare(aux[j], aux[i]) == -1:
            j += 1
            xs[k] = aux[j]
        else:
            i += 1
            xs[k] = aux[i]


def __merge_sort(xs, lo, hi, compare=default_cmp):
    if hi <= lo:
        return
    mid = lo + (hi - lo) / 2
    __merge_sort(xs, lo, mid)
    __merge_sort(xs, mid+1, hi)
    __merge(xs, lo, mid, hi, compare)


def merge_sort(xs, compare=default_cmp):
    __merge_sort(xs, 0, len(xs) - 1, compare)


