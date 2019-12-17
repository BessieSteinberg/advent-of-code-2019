from math import floor

def get_module_fuel(mass):
	# Returns (int) of required fuel for given mass of a module

	return floor( mass / 3 ) - 2

def get_module_fuel_recursive(mass):
	# Returns the amount of fuel required to get this mass movin'
	# AND the fuel required to fuel the fuel (negative fuel is ignored)

	fuel_mass = get_module_fuel(mass)

	if fuel_mass <= 0:
		return 0

	return fuel_mass + get_module_fuel_recursive(fuel_mass)
	

def get_total_fuel(masses, fuel_mass_func=get_module_fuel):
	# Returns total fuel required for the given list of masses

	fuel_sum = 0

	for mass in masses:
		fuel_sum += fuel_mass_func(mass)

	return fuel_sum