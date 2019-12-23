from main import OrbitGraph

orbit_graph = OrbitGraph('data.txt')

print(f"Checksum: {orbit_graph.num_orbits()}")
