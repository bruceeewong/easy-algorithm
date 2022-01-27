import unittest


def greedy(stations: dict, states_needed: set):
    """
    find the minimum answer that can cover all the states needed greedily
    """
    final_stations = set()  # the answer
    rest_states_needed = states_needed  # rest states that need to be covered
    while rest_states_needed:
        best_station = None
        best_station_covered = set()
        # find the station which has the widest cover range
        for station, states_for_station in stations.items():
            # get current station's intersection of states
            covered = rest_states_needed & states_for_station
            # compare with the temp station's best cover
            if len(covered) > len(best_station_covered):
                best_station = station
                best_station_covered = covered
        final_stations.add(best_station)  # append the best station for this step
        rest_states_needed -= best_station_covered  # reduce the cover needed range
    return final_stations


class TestGreedy(unittest.TestCase):
    def test(self):
        states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

        stations = {}
        stations["kone"] = set(["id", "nv", "ut"])
        stations["ktwo"] = set(["wa", "id", "mt"])
        stations["kthree"] = set(["or", "nv", "ca"])
        stations["kfour"] = set(["nv", "ut"])
        stations["kfive"] = set(["ca", "az"])

        expect = set(['ktwo', 'kthree', 'kone', 'kfive'])

        self.assertEqual(expect, greedy(stations, states_needed))
