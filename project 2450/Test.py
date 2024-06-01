import unittest
from unittest.mock import patch

# Importing the functions from the UVSim module if they were in a separate file
# from uvsim import load_program, read, write, load, store, add, subtract, divide, multiply, branch, branchneg, branchzero, halt, execute_instruction, run

class TestUVSim(unittest.TestCase):
    
    def setUp(self):
        # This method will run before each test
        global memory, accumulator, instruction_counter
        memory = [0] * 100
        accumulator = 0
        instruction_counter = 0

    def test_load_program(self):
        program = [1007, 2007, 2108, 1108, 4300]
        load_program(program)
        assert memory[:5] == program
        assert memory[5:] == [0] * 95

    def test_read(self):
        operand = 7
        with patch('builtins.input', return_value='1234'):
            read(operand)
        assert memory[operand] == 1234

    def test_write(self):
        operand = 8
        memory[operand] = 5678
        with patch('builtins.print') as mock_print:
            write(operand)
            mock_print.assert_called_with(5678)

    def test_load(self):
        operand = 9
        memory[operand] = 4321
        load(operand)
        assert accumulator == 4321

    def test_store(self):
        global accumulator
        operand = 10
        accumulator = 8765
        store(operand)
        assert memory[operand] == 8765

    def test_add(self):
        global accumulator
        operand = 11
        memory[operand] = 1111
        accumulator = 2222
        add(operand)
        assert accumulator == 3333

    def test_subtract(self):
        global accumulator
        operand = 12
        memory[operand] = 1111
        accumulator = 3333
        subtract(operand)
        assert accumulator == 2222

    def test_divide_success(self):
        global accumulator
        operand = 13
        memory[operand] = 2
        accumulator = 10
        divide(operand)
        assert accumulator == 5

    def test_divide_by_zero(self):
        global accumulator
        operand = 14
        memory[operand] = 0
        accumulator = 10
        with patch('builtins.print') as mock_print:
            divide(operand)
            mock_print.assert_called_with("Error: Division by zero")

    def test_multiply(self):
        global accumulator
        operand = 15
        memory[operand] = 3
        accumulator = 4
        multiply(operand)
        assert accumulator == 12

    def test_branch(self):
        global instruction_counter
        operand = 20
        assert branch(operand)
        assert instruction_counter == operand

    def test_branchneg(self):
        global accumulator, instruction_counter
        operand = 21
        accumulator = -1
        assert branchneg(operand)
        assert instruction_counter == operand
        accumulator = 1
        assert not branchneg(operand)

    def test_branchzero(self):
        global accumulator, instruction_counter
        operand = 22
        accumulator = 0
        assert branchzero(operand)
        assert instruction_counter == operand
        accumulator = 1
        assert not branchzero(operand)

    def test_halt(self):
        with patch('builtins.print') as mock_print:
            assert halt()
            mock_print.assert_called_with("Program halted.")

    def test_execute_instruction(self):
        global memory, instruction_counter
        memory[0] = 1007  # READ
        with patch('builtins.input', return_value='1234'):
            assert not execute_instruction(memory[0])
        assert memory[7] == 1234

    def test_run(self):
        global instruction_counter
        program = [1007, 2007, 2108, 1108, 4300]
        load_program(program)
        with patch('builtins.input', return_value='1234'):
            with patch('builtins.print') as mock_print:
                run()
                mock_print.assert_called_with(1234)
                assert instruction_counter == 5

if __name__ == '__main__':
    unittest.main()
