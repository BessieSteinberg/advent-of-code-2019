from main import IntComputer

import unittest
import pytest

@pytest.mark.parametrize("start_memory, expected_end_memory", [
	([1,0,0,0,99], [2,0,0,0,99]),
	([2,3,0,3,99], [2,3,0,6,99]),
	([2,4,4,5,99,0], [2,4,4,5,99,9801]),
	([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])
])
def test_int_computer(start_memory, expected_end_memory):

	int_computer = IntComputer(start_memory)
	int_computer.run_program()

	assert int_computer.memory == expected_end_memory
