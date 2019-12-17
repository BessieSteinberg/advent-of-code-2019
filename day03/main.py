class Pos():
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


def closest_crossing(wire_path1, wire_path2):
	# Return manhattan distance between starting point and closests crossing

	path1 = set(route_generator(wire_path1))
	path2 = set(route_generator(wire_path2))

	crossings = path1.intersection(path2)

	distances = [abs(c[0]) + abs(c[1]) for c in crossings]
	distances.sort()

	return distances[0]





	




