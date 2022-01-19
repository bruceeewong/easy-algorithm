import unittest


def quicksort(arr):
    """Quick Sort

    base condition:
        arr contains 0 or 1 element, it is already sorted
    recursive condition:
        select pivot: choose the first element
        partitioning: move less ones to pivot's left, move greater ones to pivot's right
        merge: combine less + pivot + greater

    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less_arr = [i for i in arr[1:] if i < pivot]
    greater_arr = [i for i in arr[1:] if i > pivot]
    return quicksort(less_arr) + pivot + quicksort(greater_arr)


class TestQuickSort(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5], quicksort([3, 2, 4, 5, 1]))
