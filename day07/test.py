from main import IntComputer, amp_output, best_amp_setting_sequence

import pytest


@pytest.mark.parametrize("start_memory, expected_end_memory", [
    ([1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99]),
    ([11101, 6, 7, 0, 99], [13, 6, 7, 0, 99]),
])
def test_int_computer(start_memory, expected_end_memory):
    int_computer = IntComputer(start_memory)
    int_computer.run_program()

    assert int_computer.memory == expected_end_memory


@pytest.mark.parametrize("start_memory, expected_end_memory, input_values, output_values", [
    ([3, 1, 99], [3, 42, 99], [42], []),
    ([4, 3, 99, -78], [4, 3, 99, -78], [], [-78]),
    ([3, 5, 4, 5, 99, 0], [3, 5, 4, 5, 99, -123], [-123], [-123]),
    ([3, 5, 3, 6, 99, 0, 0], [3, 5, 3, 6, 99, 8, 9], [8, 9], []),
    ([4, 5, 4, 6, 99, 12, 34], [4, 5, 4, 6, 99, 12, 34], [], [12, 34])
])
def test_int_computer_with_inputs(start_memory, expected_end_memory, input_values, output_values):
    int_computer = IntComputer(start_memory)
    outputs = int_computer.run_program(inputs=input_values)

    assert int_computer.memory == expected_end_memory

    assert output_values == outputs


@pytest.mark.parametrize("start_memory, expected_end_memory", [
    ([1, 5, 6, 7, 99, 12, 34, 0], [1, 5, 6, 7, 99, 12, 34, 46]),
    ([101, 5, 6, 7, 99, 12, 34, 0], [101, 5, 6, 7, 99, 12, 34, 39]),
    ([1001, 5, 6, 7, 99, 12, 34, 0], [1001, 5, 6, 7, 99, 12, 34, 18]),
    ([1101, 5, 6, 7, 99, 12, 34, 0], [1101, 5, 6, 7, 99, 12, 34, 11]),
    ([11001, 5, 6, 7, 99, 12, 34, 0], [11001, 5, 6, 7, 99, 12, 34, 18]),
    ([11101, 5, 6, 7, 99, 12, 34, 0], [11101, 5, 6, 7, 99, 12, 34, 11]),

])
def test_int_computer_parameter_modes(start_memory, expected_end_memory):
    int_computer = IntComputer(start_memory)
    int_computer.run_program()

    assert int_computer.memory == expected_end_memory

@pytest.mark.parametrize("start_memory, inputs, outputs", [
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8], [1]),
    ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [4], [0]),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [7], [1]),
    ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [8], [0]),
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [8], [1]),
    ([3, 3, 1108, -1, 8, 3, 4, 3, 99], [9], [0]),
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [-4], [1]),
    ([3, 3, 1107, -1, 8, 3, 4, 3, 99], [9], [0]),
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [0], [0]),
    ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], [99], [1]),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [0], [0]),
    ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [-2], [1]),
    ([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4,
      20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [7], [999]),
    ([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4,
      20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [8], [1000]),
    ([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4,
      20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], [9], [1001]),

])
def test_conditional_operations(start_memory, inputs, outputs):
    int_computer = IntComputer(start_memory)
    actual_outputs = int_computer.run_program(inputs=inputs)

    assert actual_outputs == outputs


@pytest.mark.parametrize("program, setting_sequence, expected_output", [
    [
        [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
        [4, 3, 2, 1, 0],
        43210
    ],
    [
        [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
        [0, 1, 2, 3, 4],
        54321
    ],
    [
        [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0],
        [1, 0, 4, 3, 2],
        65210
    ]
])
def test_amp_output(program, setting_sequence, expected_output):
    assert amp_output(setting_sequence, program) == expected_output

@pytest.mark.parametrize("program, setting_sequence", [
    [
        [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
        [4, 3, 2, 1, 0]
    ],
    [
        [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
        [0, 1, 2, 3, 4]
    ],
    [
        [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0],
        [1, 0, 4, 3, 2]
    ]
])
def test_best_sequence(program, setting_sequence):
    assert best_amp_setting_sequence(program) == setting_sequence