import unittest


def find_smallest(arr):
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """Selection Sort

    sort the arr by selection sort algorithm, return array that sorted by asc order

    Complexity
    - Best case: O(n)
    - Worst case: O(n^2)
    - Average case: O(n^2)

    :param arr:
    :return:
    """
    copy_arr = [*arr]
    new_arr = []
    for i in range(len(copy_arr)):
        smallest_index = find_smallest(copy_arr)
        new_arr.append(copy_arr.pop(smallest_index))
    return new_arr


class TestSelectionSort(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5], selection_sort([4, 3, 2, 5, 1]))
