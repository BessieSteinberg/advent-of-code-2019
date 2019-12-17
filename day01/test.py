from main import get_module_fuel, get_total_fuel, get_module_fuel_recursive

import unittest
import pytest

@pytest.mark.parametrize("mass, expected_fuel", [
	(12, 2),
	(14, 2),
	(1969, 654),
	(100756, 33583)
])
def test_required_fuel(mass, expected_fuel):
	actual_fuel = get_module_fuel(mass)
	assert actual_fuel == expected_fuel


def test_total_fuel():
	masses = [12, 14, 1969, 100756]
	assert get_total_fuel(masses) == 34241

@pytest.mark.parametrize("mass, expected_fuel", [
	(14, 2),
	(1969, 966),
	(100756, 50346)
])
def test_get_module_fuel_and_itself(mass, expected_fuel):
	actual_fuel = get_module_fuel_recursive(mass)
	assert actual_fuel == expected_fuel


def get_total_fuel_recursive():
	masses = [14, 1969, 100756]
	actual_fuel = get_total_fuel(masses, get_module_fuel_recursive)
	assert actual_fuel == 50346