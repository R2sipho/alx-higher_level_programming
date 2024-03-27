#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in the list_of_integers using a binary search approach.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: The peak element found in the list.
            None if the list is empty or None.
    """
    if not list_of_integers:
        return None

    def binary_search(lo, hi):
        """Performs binary search to find the peak."""
        mid = (lo + hi) // 2
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search(lo, mid - 1)
        else:
            return binary_search(mid + 1, hi)

    return binary_search(0, len(list_of_integers) - 1)
