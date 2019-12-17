

class IntComputer():

	def __init__(self, memory):
		self.memory = memory
		self.ptr = 0
		self.continue_program = True

	def get_next_int(self):
		# Return next int and increase pointer
		next_int = self.memory[self.ptr]
		self.ptr += 1
		return next_int

	def add(self):
		operand1_pos = self.get_next_int()
		operand2_pos = self.get_next_int()
		save_pos = self.get_next_int()

		operand1_val = self.memory[operand1_pos]
		operand2_val = self.memory[operand2_pos]

		self.memory[save_pos] = operand1_val + operand2_val

	def mult(self):
		operand1_pos = self.get_next_int()
		operand2_pos = self.get_next_int()
		save_pos = self.get_next_int()

		operand1_val = self.memory[operand1_pos]
		operand2_val = self.memory[operand2_pos]

		self.memory[save_pos] = operand1_val * operand2_val

	def halt(self):
		self.continue_program = False

	def operation(self, opcode):
		# Returns the operation for a given opcode
		directory = {
			1:	self.add,
			2:	self.mult,
			99: self.halt,
		}

		try:
			return directory[opcode]
		except KeyError:
			print(f"[{opcode}] is not valid opcode")
			raise

	def run_program(self):

		while self.continue_program:
			# read next opcode and increment pointer
			opcode = self.get_next_int()

			self.operation(opcode)()
