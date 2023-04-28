#!/usr/bin/python3
"""searches for the peak in an unsorted list of integers"""
anmdjfnvjn

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers.
    Arg:
        a list containing integers.
    """
    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return _find_peak(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]


def _find_peak(lint, start, stop):
    """Recursively finds peak
    Arg:
        lint, start, stop.
    """
    if stop - start < 2:
        return None
    mid = (start + stop) // 2
    if lint[mid] >= lint[mid - 1] and lint[mid] >= lint[mid + 1]:
        return lint[mid]
    return _find_peak(lint, start, mid) or _find_peak(lint, mid, stop)
