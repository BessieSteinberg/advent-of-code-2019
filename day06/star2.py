from main import OrbitGraph

orbit_graph = OrbitGraph('data.txt')
min_orbit_transfers = orbit_graph.min_orbit_transfers('YOU', 'SAN')

print(f"Minimum Orbit Transfers: {min_orbit_transfers}")