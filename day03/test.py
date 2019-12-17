from main import route_generator

import unittest
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