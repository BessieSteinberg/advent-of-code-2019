class IntComputer:

    def __init__(self, memory):
        self.memory = memory
        self.ptr = 0
        self.continue_program = True
        self.inputs = []
        self.outputs = []

    def get_next_int(self):
        # Return next int and increase pointer
        next_int = self.memory[self.ptr]
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

    def get_parameters(self, param_modes):
        """
        Generates the next parameters based on the current position of the program pointer.
        Args:
            param_modes: (list) list of bools for each parameter.  If param_modes[X] is True
                than parameter X is in immediate mode and that value can be used as is.  Otherwise
                that value refers to the memory address where that value is stored.

        Returns:
            params: (list)  list of parameters
        """

        params = []
        for param_mode in param_modes:
            param = self.get_next_int()

            if not param_mode:
                # param is in position mode
                param = self.memory[param]

            params.append(param)

        return params

    def add(self, parameter_modes):
        """
        Adds two operands and saves to the given position
        Args:
            parameters: (list)  list of bools describing which mode each parameter is in in
                the format: [operand_1, operand_2, position_to_save]
        """
        # import pudb; pudb.set_trace()

        # Parameters that refer to a write-to address are always in immediate mode
        parameter_modes[2] = True
        parameters = self.get_parameters(parameter_modes)

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.memory[save_pos] = operand1_val + operand2_val

    def mult(self, parameter_modes):
        """
        Multiplies two operands and saves to the given position
        Args:
            parameter_modes: (list)  list of bools describing which mode each parameter is in in
                the format: [operand_1, operand_2, position_to_save]
        """
        # import pudb; pudb.set_trace()

        # Parameters that refer to a write-to address are always in immediate mode
        parameter_modes[2] = True
        parameters = self.get_parameters(parameter_modes)

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.memory[save_pos] = operand1_val * operand2_val

    def jump_if_true(self, parameter_modes):
        """
        If the first parameter is not 0 sets the program pointer to the value in the second parameter
        Args:
            parameter_modes:(list)  list of bools describing which mode each parameter is in in
                the format: [operand, pointer_position]
        """
        # import pudb; pudb.set_trace()

        # this operation only needs 2 parameters
        parameters = self.get_parameters(parameter_modes[:2])

        operand_val = parameters[0]
        jump_pos = parameters[1]

        if operand_val != 0:
            self.ptr = jump_pos

    def jump_if_false(self, parameter_modes):
        """
        If the first parameter is 0 sets the program pointer to the value in the second parameter
        Args:
            parameter_modes:(list)  list of bools describing which mode each parameter is in in
                the format: [operand, pointer_position]
        """
        # import pudb; pudb.set_trace()

        # this operation only needs 2 parameters
        parameters = self.get_parameters(parameter_modes[:2])

        operand_val = parameters[0]
        jump_pos = parameters[1]

        if operand_val == 0:
            self.ptr = jump_pos

    def eqls(self, parameter_modes):
        """
        Checks if the first two parameters are equal. If they are it writes '1' to a given
        position and if they aren't writes '0' to a given position.
        Args:
            parameter_modes: (list)  list of bools describing which mode each parameter is in in
                the format: [operand_1, operand_2, position_to_save]
        """
        # import pudb; pudb.set_trace()

        # Parameters that refer to a write-to address are always in immediate mode
        parameter_modes[2] = True
        parameters = self.get_parameters(parameter_modes)

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.memory[save_pos] = 1 if operand1_val == operand2_val else 0

    def less_than(self, parameter_modes):
        """
        Checks if the first parameter is less than the second. If they are it writes '1' to a given
        position and if they aren't writes '0' to a given position.
        Args:
            parameter_modes: (list)  list of bools describing which mode each parameter is in in
                the format: [operand_1, operand_2, position_to_save]
        """
        # import pudb; pudb.set_trace()

        # Parameters that refer to a write-to address are always in immediate mode
        parameter_modes[2] = True
        parameters = self.get_parameters(parameter_modes)

        operand1_val = parameters[0]
        operand2_val = parameters[1]
        save_pos = parameters[2]

        self.memory[save_pos] = 1 if operand1_val < operand2_val else 0

    def get_input(self, *args, **kwargs):
        """
        Gets the next input from the input queue and stores it into the given address
        """
        # import pudb; pudb.set_trace()
        # The next parameter is the write to address
        save_pos = self.get_next_int()
        self.memory[save_pos] = self.get_next_input()

    def write_output(self, parameter_modes):
        """
        Writes output from given memory position to the output queue
        Args:
            parameter_modes: (list)  list of bools describing which mode each parameter is in in
                the format: [output_val]
        """
        # import pudb; pudb.set_trace()
        # this operation has only one parameter
        parameters = self.get_parameters(parameter_modes[:1])
        output_val = parameters[0]
        self.outputs.append(output_val)

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
            # import pudb; pudb.set_trace()
            # read next opcode and increment pointer
            instruction_code = str(self.get_next_int())
            opcode = int(instruction_code[-2:])
            parameter_modes = instruction_code[:-2][::-1]
            while len(parameter_modes) < 3:
                parameter_modes = parameter_modes + '0'

            self.operation(opcode)(['1' == pm for pm in parameter_modes])

        return self.outputs