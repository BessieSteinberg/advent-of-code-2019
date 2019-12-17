from main import total_fuel

with open('input.txt', 'r') as f:
	data = f.readlines()

data = [int(d) for d in data]

fuel_required = total_fuel(data)

print(f"total fuel required: {fuel_required}")