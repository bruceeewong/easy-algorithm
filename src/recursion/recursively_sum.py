import unittest


def sum_recursively(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_recursively(arr[1:])


class TestRecursivelySum(unittest.TestCase):
    def test(self):
        self.assertEqual(0, sum_recursively([]))
        self.assertEqual(1, sum_recursively([1]))
        self.assertEqual(9, sum_recursively([1, 3, 5]))
