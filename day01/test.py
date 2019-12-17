from main import module_fuel, total_fuel

import unittest
import pytest

@pytest.mark.parametrize("mass, expected_fuel", [
	(12, 2),
	(14, 2),
	(1969, 654),
	(100756, 33583)
])
def test_required_fuel(mass, expected_fuel):
	actual_fuel = module_fuel(mass)
	assert actual_fuel == expected_fuel


def test_total_fuel():
	masses = [12, 14, 1969, 100756]
	assert total_fuel(masses) == 34241

