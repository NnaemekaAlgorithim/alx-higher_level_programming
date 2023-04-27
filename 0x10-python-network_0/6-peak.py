#!/usr/bin/python3
"""searches for the peak in an unsorted list of integers"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers.
    Arg:
        a list containing integers.
    """
    loi = list_of_integers
    if loi == []:
        return None
    total = len(loi)
    if total == 1:
        return loi[0]
    elif total == 2:
        return max(loi)
    middle = int(total / 2)
    peak = loi[middle]
    if peak > loi[middle - 1] and peak > loi[middle + 1]:
        return peak
    elif peak < loi[middle - 1]:
        return find_peak(loi[:middle])
    else:
        return find_peak(loi[middle + 1:])
