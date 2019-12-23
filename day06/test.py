from main import OrbitGraph

import pytest


@pytest.mark.parametrize("file, num_orbits", [
    ('test_data.txt', 42),
    ('test2_data.txt', 41),
])
def test_orbit_graph(file, num_orbits):
    orbit_graph = OrbitGraph(file)
    assert orbit_graph.num_orbits() == num_orbits
