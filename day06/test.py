from main import OrbitGraph

import pytest


@pytest.mark.parametrize("file, num_orbits", [
    ('test_data.txt', 42),
    ('test2_data.txt', 41),
])
def test_orbit_graph(file, num_orbits):
    orbit_graph = OrbitGraph(file)
    assert orbit_graph.num_orbits() == num_orbits


def test_most_recent_shared_ancestor():
    orbit_graph = OrbitGraph('test3_data.txt')
    orbit_graph.most_recent_shared_ancestor('YOU', 'SAN') == 'D'


@pytest.mark.parametrize("file, planet1, planet2, transfers", [
    ['test3_data.txt', 'YOU', 'SAN', 4],
    ['test2_data.txt', 'NOP', 'JKL', 5],
    ['test2_data.txt', 'FGH', 'JKL', 4],
])
def test_min_orbit_transfers(file, planet1, planet2, transfers):
    orbit_graph = OrbitGraph(file)
    orbit_graph.min_orbit_transfers(planet1, planet2) == 5
