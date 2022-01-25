import unittest
from collections import deque
from inspect import isfunction


def breadth_first_search(graph, start, is_target):
    if not isfunction(is_target):
        return False
    search_queue = deque()
    search_queue += graph[start]
    searched = []

    while search_queue:
        item = search_queue.popleft()
        if item in searched:
            continue
        if is_target(item):
            return True
        else:
            search_queue += graph[item]
            searched.append(item)
    return False


class TestBreadthFirstSearch(unittest.TestCase):
    def test(self):
        graph = {}
        graph["you"] = ["alice", "bob", "claire"]
        graph["bob"] = ["anuj", "peggy"]
        graph["alice"] = ["peggy"]
        graph["claire"] = ["thom", "jonny"]
        graph["anuj"] = []
        graph["peggy"] = []
        graph["thom"] = []
        graph["jonny"] = []

        self.assertEqual(True, breadth_first_search(graph, 'you', lambda x: x == 'bob'))
        self.assertEqual(True, breadth_first_search(graph, 'you', lambda x: x == 'peggy'))
        self.assertEqual(True, breadth_first_search(graph, 'you', lambda x: x == 'anuj'))
        self.assertEqual(True, breadth_first_search(graph, 'you', lambda x: x == 'thom'))
