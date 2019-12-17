from main import get_total_fuel, get_module_fuel_recursive

with open('input.txt', 'r') as f:
	data = f.readlines()

data = [int(d) for d in data]

fuel_required = get_total_fuel(data, get_module_fuel_recursive)

print(f"total fuel required: {fuel_required}")