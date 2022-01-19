import unittest


def count_list_recursively(arr):
    """
    Count all the elements even nested in array
    :param arr:
    :return:
    """
    result = 0
    for item in arr:
        if not isinstance(item, list):
            result += 1
        else:
            result += count_list_recursively(item)
    return result


class TestRecursivelySum(unittest.TestCase):
    def test(self):
        self.assertEqual(0, count_list_recursively([]))
        self.assertEqual(1, count_list_recursively([1]))
        self.assertEqual(3, count_list_recursively([1, 3, 5]))
        self.assertEqual(3, count_list_recursively([[1], 3, 5]))
        self.assertEqual(5, count_list_recursively([[1, [1, 2]], 3, 5]))
