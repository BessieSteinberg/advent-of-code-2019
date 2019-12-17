from main import route_generator, closest_crossing, closest_crossing_in_steps

import pytest


@pytest.mark.parametrize("wire_path, expected_route", [
	(
		"R8,U5,L5,D3",
		[
			(1, 0),
			(2, 0),
			(3, 0),
			(4, 0),
			(5, 0),
			(6, 0),
			(7, 0),
			(8, 0),
			(8, 1),
			(8, 2),
			(8, 3),
			(8, 4),
			(8, 5),
			(7, 5),
			(6, 5),
			(5, 5),
			(4, 5),
			(3, 5),
			(3, 4),
			(3, 3),
			(3, 2)
		]
	),
	(
		"U7,R6,D4,L4",
		[
			(0, 1),
			(0, 2),
			(0, 3),
			(0, 4),
			(0, 5),
			(0, 6),
			(0, 7),
			(1, 7),
			(2, 7),
			(3, 7),
			(4, 7),
			(5, 7),
			(6, 7),
			(6, 6),
			(6, 5),
			(6, 4),
			(6, 3),
			(5, 3),
			(4, 3),
			(3, 3),
			(2, 3)
		]
	)
])
def test_route_generator(wire_path, expected_route):

	gen = route_generator(wire_path)
	actual_route = list(gen)

	assert actual_route == expected_route


@pytest.mark.parametrize("wire_path1, wire_path2, distance", [
	(
		"R75,D30,R83,U83,L12,D49,R71,U7,L72",
		"U62,R66,U55,R34,D71,R55,D58,R83",
		159
	),
	(
		"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
		"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
		135
	)
])
def test_closets_crossing(wire_path1, wire_path2, distance):
	assert closest_crossing(wire_path1, wire_path2) == distance


@pytest.mark.parametrize("wire_path1, wire_path2, steps", [
	# (
	# 	"R8,U5,L5,D3",
	# 	"U7,R6,D4,L4",
	# 	30
	# ),
	(
		"R75,D30,R83,U83,L12,D49,R71,U7,L72",
		"U62,R66,U55,R34,D71,R55,D58,R83",
		610
	),
	# (
	# 	"R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
	# 	"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
	# 	410
	# )
])
def test_closest_crossing_in_steps(wire_path1, wire_path2, steps):
	assert closest_crossing_in_steps(wire_path1, wire_path2) == steps

