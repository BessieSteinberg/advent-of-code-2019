from itertools import count

class Pos:
	def __init__(self):
		self.x = 0
		self.y = 0
	
	def value(self):
		return (self.x, self.y)

	def go_right(self):
		self.x += 1

	def go_left(self):
		self.x -= 1

	def go_up(self):
		self.y += 1

	def go_down(self):
		self.y -= 1

	def go(self, direction):

		go = {
			'R': self.go_right,
			'L': self.go_left,
			'U': self.go_up,
			'D': self.go_down,
		}
		go[direction]()


def route_generator(wire_path):

	pos = Pos()

	wire_path = wire_path.split(',')

	for vector in wire_path:
		
		direction = vector[0]
		scale = int(vector[1:])

		for step in range(scale):
			pos.go(direction)
			yield pos.value()


def get_crossings(wire_path1, wire_path2):
	# Return (set) of crossings
	path1 = set(route_generator(wire_path1))
	path2 = set(route_generator(wire_path2))

	return path1.intersection(path2)


def closest_crossing(wire_path1, wire_path2):
	# Return manhattan distance between starting point and closests crossing
	crossings = get_crossings(wire_path1, wire_path2)

	distances = [abs(c[0]) + abs(c[1]) for c in crossings]
	distances.sort()

	return distances[0]


def closest_crossing_in_steps(wire_path1, wire_path2):
	# Return the total number of steps it takes to get wire 1 and wire 2 to their closest crossing

	# for each given position, provide the number of steps to get there the first time
	steps1 = {}
	step_counter = count(1)

	for pos in route_generator(wire_path1):
		current_step = next(step_counter)

		# if this pos has not been visited yet create an entry for it
		if not steps1.get(pos):
			steps1[pos] = current_step

	steps2 = {}
	step_counter = count(1)

	for pos in route_generator(wire_path1):
		current_step = next(step_counter)

		# if this pos has not been visited yet create an entry for it
		if not steps2.get(pos):
			steps2[pos] = current_step

	crossings = get_crossings(wire_path1, wire_path2)

	steps_to_crossings = [steps1[crossing] + steps2[crossing] for crossing in crossings]
	steps_to_crossings.sort()

	return steps_to_crossings[0]


	




