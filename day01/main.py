from math import floor

def module_fuel(mass):
	# Returns (int) of required fuel for given mass of a module

	return floor( mass / 3 ) - 2

def total_fuel(masses):
	# Returns total fuel required for the given list of masses
	# TODO: turn into list comprehension

	fuel_sum = 0

	for mass in masses:
		fuel_sum += module_fuel(mass)

	return fuel_sum