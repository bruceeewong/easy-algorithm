import unittest


def dijkstra(graph, costs, parents):
    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


class TestDijkstra(unittest.TestCase):
    def test(self):
        graph = {}
        graph["a"] = {}
        graph["a"]["fin"] = 1
        graph["b"] = {}
        graph["b"]["a"] = 3
        graph["b"]["fin"] = 5
        graph["fin"] = {}

        inf = float('inf')
        costs = {}
        costs['a'] = 6
        costs['b'] = 2
        costs['fin'] = inf

        parents = {}
        parents['a'] = 'start'
        parents['b'] = 'start'
        parents['fin'] = None

        result = {
            "path": ['start', 'b', 'a', 'fin'],
            "lowest_cost": 5
        }

        dijkstra(graph, costs, parents)
        self.assertEqual(6, costs['fin'])
        self.assertEqual(2, costs['b'])
        self.assertEqual(5, costs['a'])
