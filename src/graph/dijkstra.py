import unittest

# def dijkstra(graph, costs, parents):
#     processed = []
#
#     def find_lowest_cost_node(costs):
#         lowest_cost = float('inf')
#         lowest_cost_node = None
#         for node in costs:
#             cost = costs[node]
#             if cost < lowest_cost and node not in processed:
#                 lowest_cost = cost
#                 lowest_cost_node = node
#         return lowest_cost_node
#
#     node = find_lowest_cost_node(costs)
#     while node is not None:
#         cost = costs[node]
#         neighbors = graph[node]
#         for n in neighbors.keys():
#             new_cost = cost + neighbors[n]
#             if new_cost < costs[n]:
#                 costs[n] = new_cost
#                 parents[n] = node
#         processed.append(node)
#         node = find_lowest_cost_node(costs)

inf = float('inf')


def dijkstra(graph: dict, costs: dict, parents: dict, settings: dict):
    def find_lowest_cost_node(costs: dict, processed: list):
        lowest_cost = inf
        lowest_cost_node = None
        for node in costs.keys():
            if node in processed:
                continue
            node_cost = costs[node]
            if node_cost < lowest_cost:
                lowest_cost = node_cost
                lowest_cost_node = node
        return lowest_cost_node

    def get_lowest_cost_path(parents: dict, fin_node):
        result = []
        next = fin_node
        while next is not None:
            result.append(next)
            next = parents[next] if next in parents else None
        result.reverse()
        return result

    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        neighbors = graph[node]
        cost = costs[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    fin_node = settings.get('fin')
    result = {
        'path': get_lowest_cost_path(parents, fin_node),
        'lowest_cost': costs[fin_node]
    }
    return result


class TestDijkstra(unittest.TestCase):
    def test(self):
        graph = {}
        graph["a"] = {}
        graph["a"]["fin"] = 1
        graph["b"] = {}
        graph["b"]["a"] = 3
        graph["b"]["fin"] = 5
        graph["fin"] = {}

        costs = {}
        costs['a'] = 6
        costs['b'] = 2
        costs['fin'] = inf

        parents = {}
        parents['a'] = 'start'
        parents['b'] = 'start'
        parents['fin'] = None

        settings = {
            'fin': 'fin'
        }

        expectation = {
            "path": ['start', 'b', 'a', 'fin'],
            "lowest_cost": 6
        }

        result = dijkstra(graph, costs, parents, settings)
        self.assertEqual(6, costs['fin'])
        self.assertEqual(2, costs['b'])
        self.assertEqual(5, costs['a'])
        self.assertEqual(expectation, result)
