import unittest
from unittest.mock import patch
import program1

class TestUVSim(unittest.TestCase):
    
    def setUp(self):
        # This method will run before each test
        global memory, accumulator, instruction_counter
        program1.memory = [0] * 100
        program1.accumulator = 0
        program1.instruction_counter = 0

    # Test loading a program into memory
    def test_load_program(self):
        program = [1007, 2007, 2108, 1108, 4300]
        program1.load_program(program)
        self.assertEqual(program1.memory[:5], program)
        self.assertEqual(program1.memory[5:], [0] * 95)

    # Test reading a value into memory
    def test_read(self):
        operand = 7
        with patch('builtins.input', return_value='1234'):
            program1.read(operand)
        self.assertEqual(program1.memory[operand], 1234)

    # Test writing a value from memory
    def test_write(self):
        operand = 8
        program1.memory[operand] = 5678
        with patch('builtins.print') as mock_print:
            program1.write(operand)
            mock_print.assert_called_with(f"Output from memory location {operand}: 5678")

    # Test loading a value from memory into the accumulator
    def test_load(self):
        operand = 9
        program1.memory[operand] = 4321
        program1.load(operand)
        self.assertEqual(program1.accumulator, 4321)

    # Test storing the accumulator value into memory
    def test_store(self):
        operand = 10
        program1.accumulator = 8765
        program1.store(operand)
        self.assertEqual(program1.memory[operand], 8765)

    # Test adding a value from memory to the accumulator
    def test_add(self):
        operand = 11
        program1.memory[operand] = 1111
        program1.accumulator = 2222
        self.assertEqual(program1.add(operand), 3333)

    # Test subtracting a value from memory from the accumulator
    def test_subtract(self):
        operand = 12
        program1.memory[operand] = 1111
        program1.accumulator = 3333
        program1.subtract(operand, test=program1.memory[operand])
        self.assertEqual(program1.accumulator, 2222)

    # Test dividing the accumulator by a value from memory (success case)
    def test_divide_success(self):
        operand = 13
        program1.memory[operand] = 2
        program1.accumulator = 10
        program1.divide(operand, test=program1.memory[operand])
        self.assertEqual(program1.accumulator, 5)

    # Test dividing the accumulator by zero (failure case)
    def test_divide_by_zero(self):
        operand = 14
        program1.memory[operand] = 0
        program1.accumulator = 10
        with patch('builtins.print') as mock_print:
            program1.divide(operand)
            mock_print.assert_called_with("Error: Division by zero")

    # Test multiplying the accumulator by a value from memory
    def test_multiply(self):
        operand = 15
        program1.memory[operand] = 3
        program1.accumulator = 4
        program1.multiply(operand, test=program1.memory[operand])
        self.assertEqual(program1.accumulator, 12)

    # Test unconditional branch to a memory location
    def test_branch(self):
        operand = 20
        program1.branch(operand)
        self.assertEqual(program1.instruction_counter, operand)

    # Test branch to a memory location if the accumulator is negative
    def test_branchneg(self):
        operand = 21
        program1.accumulator = -1
        self.assertTrue(program1.branchneg(operand))
        self.assertEqual(program1.instruction_counter, operand)
        program1.accumulator = 1
        self.assertFalse(program1.branchneg(operand))

    # Test branchneg with a positive accumulator (no branching)
    def test_branchneg_positive_accumulator(self):
        operand = 23
        program1.accumulator = 1
        self.assertFalse(program1.branchneg(operand))
        self.assertNotEqual(program1.instruction_counter, operand)

    # Test branch to a memory location if the accumulator is zero
    def test_branchzero(self):
        operand = 22
        program1.accumulator = 0
        self.assertTrue(program1.branchzero(operand))
        self.assertEqual(program1.instruction_counter, operand)
        program1.accumulator = 1
        self.assertFalse(program1.branchzero(operand))

    # Test branchzero with a non-zero accumulator (no branching)
    def test_branchzero_non_zero_accumulator(self):
        operand = 24
        program1.accumulator = 5
        self.assertFalse(program1.branchzero(operand))
        self.assertNotEqual(program1.instruction_counter, operand)

    # Test halting the program
    def test_halt(self):
        with patch('builtins.print') as mock_print:
            self.assertTrue(program1.halt())
            mock_print.assert_called_with("Program halted.")

    # Test executing a single instruction (READ)
    def test_execute_instruction(self):
        program1.memory[0] = 1007  # READ
        with patch('builtins.input', return_value='1234'):
            self.assertFalse(program1.execute_instruction(program1.memory[0]))
        self.assertEqual(program1.memory[7], 1234)

    # Test running a program
    def test_run(self):
        program = [1007, 2007, 2108, 1108, 4300]
        program1.load_program(program)
        with patch('builtins.input', return_value='1234'):
            with patch('builtins.print') as mock_print:
                program1.run()
                mock_print.assert_called_with("Final accumulator value: 1234")

    # Test running a specific program
    def test_run_specific_program(self):
        program = [1007, 2007, 3108, 1108, 4300]
        program1.load_program(program)
        with patch('builtins.input', return_value='1234'):
            with patch('builtins.print') as mock_print:
                program1.run()
                mock_print.assert_any_call("Program halted.")

    # Test reading a program from a valid file
    def test_read_program_from_file_valid(self):
        with patch('builtins.open', unittest.mock.mock_open(read_data='1007\n2007\n3108\n1108\n4300')):
            program = program1.read_program_from_file('dummy_file.txt')
            self.assertEqual(program, [1007, 2007, 3108, 1108, 4300])

if __name__ == '__main__':
    unittest.main()
