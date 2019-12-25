class IntComputer:

    def __init__(self, memory):
        self.memory = memory
        self.extended_memory = {}
        self.ptr = 0
        self.relative_base = 0
        self.continue_program = True
        self.inputs = []
        self.outputs = []

    def read_from_memory(self, address):
        """
        Access memory at location 'address'.  If the address is over the normal range use extended memory.
        If address is negative throw an error.
        Args:
            address: (int) memory address

        Returns:
            (int) value at that range
        """

        if address < 0:
            print("Address values cannot be negative!")
            raise

        try:
            return self.memory[address]
        except IndexError:
            try:
                return self.extended_memory[address]
            except KeyError:
                # This spot in memory does not exist so create it
                self.extended_memory[address] = 0
                return self.extended_memory[address]

    def write_to_memory(self, address, value):
        """
        Write value to memory the address location
        Args:
            address: (int)  address to write to
            value: (int)    value to write to that address
        """
        try:
            self.memory[address] = value
        except IndexError:
            self.extended_memory[address] = value

    def get_next_int(self):
        # Return next int and increase pointer
        next_int = self.read_from_memory(self.ptr)
        self.ptr += 1
        return next_int

    def get_next_input(self):
        """
        Pops the next input of the input queue
        Returns:
            next_input: (int) next input
        """

        try:
            return self.inputs.pop(0)
        except AttributeError:
            print(f"There is no input queue!")
            raise

    def get_parameters(self, param_modes, num_params, literal_mode=False):
        """
        Generates the next parameters based on the current position of the program pointer.
        Args:
            param_modes: (str)  string of 0-2s representing the mode each parameter must be read in.
                0: position mode: this means get the value at this memory address
                1: immediate mode: this means get the value as is
                2: relative mode: this means get the value at the memory address <relative offset> + <this value>
                example: if param_modes is '210' that would mean the first param is read in position mode, the second
                is read in immediate mode and the third in relative mode
                If there are less values then the num_params then the remaining params are assumed to be in position
                mode
            num_params: (int)   number of parameters to get
            literal_mode: (bool)    if True the last value is in literal mode. if the mode is 0 or 1 take the value as
                is. If it's 2 value + relative offset

        Returns:
            params: (list)  list of parameters
        """
        postion_mode = 0
        immediate_mode = 1
        relative_mode = 2

        literal_immediate_mode = 11
        literal_relative_mode = 12

        modes = [postion_mode for __ in range(num_params)]

        for i in range(len(param_modes)):
            modes[i] = int(param_modes[i])

        if literal_mode:
            if modes[-1] is postion_mode or modes[-1] is immediate_mode:
                modes[-1] = literal_immediate_mode
            elif modes[-1] is relative_mode:
                modes[-1] = literal_relative_mode

        params = []
        for mode in modes:
            param = self.get_next_int()

            if mode is postion_mode:
                param = self.read_from_memory(param)
            elif mode is relative_mode:
                param = self.read_from_memory(self.relative_base + param)
            elif mode is literal_relative_mode:
                param = self.relative_base + param

            params.append(param)

        return params

    def add(self, parameter_modes):
        """
        Format: 1, operand_1, operand_2, position_to_save
        Adds two operands and saves to the given position
        Args:
            parameter_modes: (list)  list of bools describing which mode each parameter is in in
                the format: [operand_1, operand_2, position_to_save]
        """
        # import pudb; pudb.set_trace()

        parameters = self.get_parameters(parameter_modes, 3, [2])

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.write_to_memory(save_pos, operand1_val + operand2_val)

    def mult(self, parameter_modes):
        """
        Format: 2, operand_1, operand_2, position_to_save
        Multiplies two operands and saves to the given position
        Args:
            parameter_modes: (str)
        """
        # import pudb; pudb.set_trace()

        parameters = self.get_parameters(parameter_modes, 3, [2])

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.write_to_memory(save_pos, operand1_val * operand2_val)

    def jump_if_true(self, parameter_modes):
        """
        Format: 5, operand, pointer_position
        If the first parameter is not 0 sets the program pointer to the value in the second parameter
        Args:
            parameter_modes:(str)
        """
        # import pudb; pudb.set_trace()

        parameters = self.get_parameters(parameter_modes, 2)

        operand_val = parameters[0]
        jump_pos = parameters[1]

        if operand_val != 0:
            self.ptr = jump_pos

    def jump_if_false(self, parameter_modes):
        """
        Format: 6, operand, pointer_position
        If the first parameter is 0 sets the program pointer to the value in the second parameter
        Args:
            parameter_modes:(str)
        """
        # import pudb; pudb.set_trace()

        parameters = self.get_parameters(parameter_modes, 2)

        operand_val = parameters[0]
        jump_pos = parameters[1]

        if operand_val == 0:
            self.ptr = jump_pos

    def eqls(self, parameter_modes):
        """
        Format: 8, operand_1, operand_2, position_to_save

        Checks if the first two parameters are equal. If they are it writes '1' to a given
        position and if they aren't writes '0' to a given position.
        Args:
            parameter_modes: (str)
        """
        # import pudb; pudb.set_trace()

        parameters = self.get_parameters(parameter_modes, 3, [2])

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.write_to_memory(save_pos, 1 if operand1_val == operand2_val else 0)

    def less_than(self, parameter_modes):
        """
        Format: 7, operand_1, operand_2, position_to_save
        Checks if the first parameter is less than the second. If they are it writes '1' to a given
        position and if they aren't writes '0' to a given position.
        Args:
            parameter_modes: (str)
        """
        # import pudb; pudb.set_trace()

        parameters = self.get_parameters(parameter_modes, 3, [2])

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.write_to_memory(save_pos, 1 if operand1_val < operand2_val else 0)

    def get_input(self, parameter_mode):
        """
        Format: 3, save_pos
        Gets the next input from the input queue and stores it into the given address
        Args:
            parameter_mode: (str)
        """
        # import pudb; pudb.set_trace()

        # The next parameter is the write to address
        save_pos = self.get_next_int()
        if parameter_mode == '2':
            # relative mode
            save_pos = self.relative_base + save_pos

        self.write_to_memory(save_pos, self.get_next_input())

    def write_output(self, parameter_modes):
        """
        Format: 4, output_val
        Writes output from given memory position to the output queue
        Args:
            parameter_modes: (str)
        """
        # import pudb; pudb.set_trace()

        parameters = self.get_parameters(parameter_modes, 1)
        output_val = parameters[0]
        self.outputs.append(output_val)

    def adjust_relative_base(self, parameter_modes):
        """
        Format: 9, relative_base_offset
        Adds the relative base offset to the current relative base
        Args:
            parameter_modes: (str)
        """
        # import pudb; pudb.set_trace()
        parameters = self.get_parameters(parameter_modes, 1)
        relative_base_offset = parameters[0]
        self.relative_base += relative_base_offset

    def halt(self, *args, **kwargs):
        self.continue_program = False

    def operation(self, opcode):
        # Returns the operation for a given opcode
        directory = {
            1:  self.add,
            2:  self.mult,
            3:  self.get_input,
            4:  self.write_output,
            5:  self.jump_if_true,
            6:  self.jump_if_false,
            7:  self.less_than,
            8:  self.eqls,
            9:  self.adjust_relative_base,
            99: self.halt,
        }

        try:
            return directory[opcode]
        except KeyError:
            print(f"[{opcode}] is not valid opcode")
            raise

    def run_program(self, inputs=None):
        if inputs:
            # reverse inputs so that pop works properly
            self.inputs = inputs

        while self.continue_program:
            # read next opcode and increment pointer
            instruction_code = str(self.get_next_int())
            # import pudb; pudb.set_trace()
            opcode = int(instruction_code[-2:])
            parameter_modes = instruction_code[:-2][::-1]

            self.operation(opcode)(parameter_modes)

        return self.outputs