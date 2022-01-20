import unittest


def combination(arr, k):
    if k == 0 or k > len(arr):
        return []

    result = []
    record_path = []

    def dfs(source, path, index):
        if len(path) == k:
            result.append(path.copy())
            return
        for i in range(index, len(source)):
            path.append(source[i])
            dfs(source, path, i + 1)
            path.pop()

    dfs(arr, record_path, 0)
    return result


class TestCombination(unittest.TestCase):
    def test(self):
        self.assertEqual([], combination(['a', 'b', 'c', 'd'], 0))
        self.assertEqual([['a'], ['b'], ['c'], ['d']], combination(['a', 'b', 'c', 'd'], 1))
        self.assertEqual([
            ['a', 'b'],
            ['a', 'c'],
            ['a', 'd'],
            ['b', 'c'],
            ['b', 'd'],
            ['c', 'd'],
        ], combination(['a', 'b', 'c', 'd'], 2))
        self.assertEqual([
            ['a', 'b', 'c'],
            ['a', 'b', 'd'],
            ['a', 'c', 'd'],
            ['b', 'c', 'd'],
        ], combination(['a', 'b', 'c', 'd'], 3))
