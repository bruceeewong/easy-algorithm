import unittest


def binary_search(arr, target):
    """Binary Search

    Find item in the array that sorted by asc order, return index
    if not found, return None

    Complexity
    - Worst case: O(logn)
    - Best case: O(1)
    - Average case: O(logn)

    :param arr:
    :param target:
    :return:
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        ele = arr[mid]
        if ele == target:
            return mid
        if ele > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


class TestBinarySearch(unittest.TestCase):
    def test(self):
        self.assertEqual(None, binary_search([], 0))
        self.assertEqual(0, binary_search([0], 0))
        self.assertEqual(1, binary_search([1, 3, 5, 7, 9], 3))
