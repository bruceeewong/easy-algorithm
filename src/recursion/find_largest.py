import unittest


def find_largest(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    sub_largest = find_largest(arr[1:])
    return arr[0] if arr[0] > sub_largest else sub_largest


class TestFindLargest(unittest.TestCase):
    def test(self):
        self.assertEqual(None, find_largest([]))
        self.assertEqual(1, find_largest([1]))
        self.assertEqual(5, find_largest([1, 5, 3]))
        self.assertEqual(7, find_largest([1, 5, 7]))
