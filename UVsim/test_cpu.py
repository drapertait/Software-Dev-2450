import unittest
from unittest.mock import Mock
import sys
import os

# Add the parent directory to the sys.path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cpu_class import CPU

class TestCPU(unittest.TestCase):
    def setUp(self):
        self.memory = Mock()
        self.output_function = Mock()
        self.cpu = CPU(self.memory, self.output_function)

    def test_read(self):
        self.output_function.return_value = '1234'
        self.cpu.read(7)
        self.memory.write.assert_called_with(7, 1234)
        self.output_function.assert_any_call("Executed read (opcode 10) on memory location 7: 1234", is_user_output=True)

    def test_write(self):
        self.memory.read.return_value = 4321
        self.cpu.write(7)
        self.output_function.assert_any_call("Executed write (opcode 11) on memory location 7: 4321", is_user_output=True)

    def test_load(self):
        self.memory.read.return_value = 1000
        self.cpu.load(10)
        self.assertEqual(self.cpu.accumulator, 1000)
        self.output_function.assert_any_call("Loaded value 1000 from memory location 10 into accumulator.")

    def test_store(self):
        self.cpu.accumulator = 2000
        self.cpu.store(10)
        self.memory.write.assert_called_with(10, 2000)
        self.output_function.assert_any_call("Stored value 2000 from accumulator into memory location 10.")

    def test_add(self):
        self.memory.read.return_value = 3000
        self.cpu.accumulator = 2000
        self.cpu.add(5)
        self.assertEqual(self.cpu.accumulator, 5000)
        self.output_function.assert_any_call("Added value from memory location 5, new accumulator value: 5000")

    def test_subtract(self):
        self.memory.read.return_value = 1000
        self.cpu.accumulator = 2000
        self.cpu.subtract(5)
        self.assertEqual(self.cpu.accumulator, 1000)
        self.output_function.assert_any_call("Subtracted value from memory location 5, new accumulator value: 1000")

    def test_divide(self):
        self.memory.read.return_value = 2
        self.cpu.accumulator = 10
        self.cpu.divide(5)
        self.assertEqual(self.cpu.accumulator, 5)
        self.output_function.assert_any_call("Divided by value from memory location 5, new accumulator value: 5")

    def test_divide_by_zero(self):
        self.memory.read.return_value = 0
        self.cpu.accumulator = 10
        self.cpu.divide(5)
        self.output_function.assert_any_call("Error: Division by zero")

    def test_multiply(self):
        self.memory.read.return_value = 3
        self.cpu.accumulator = 4
        self.cpu.multiply(5)
        self.assertEqual(self.cpu.accumulator, 12)
        self.output_function.assert_any_call("Multiplied by value from memory location 5, new accumulator value: 12")

    def test_branch(self):
        self.cpu.branch(20)
        self.assertEqual(self.cpu.instruction_counter, 20)

    def test_branchneg(self):
        self.cpu.accumulator = -10
        self.cpu.branchneg(15)
        self.assertEqual(self.cpu.instruction_counter, 15)

    def test_branchneg_no_jump(self):
        self.cpu.accumulator = 10
        self.cpu.branchneg(15)
        self.assertNotEqual(self.cpu.instruction_counter, 15)

    def test_branchzero(self):
        self.cpu.accumulator = 0
        self.cpu.branchzero(10)
        self.assertEqual(self.cpu.instruction_counter, 10)

    def test_branchzero_no_jump(self):
        self.cpu.accumulator = 5
        self.cpu.branchzero(10)
        self.assertNotEqual(self.cpu.instruction_counter, 10)

    def test_halt(self):
        self.assertTrue(self.cpu.halt())
        self.output_function.assert_any_call("Program encountered halt (43) opcode.")

    def test_overflow(self):
        self.memory.read.return_value = 5
        self.cpu.accumulator = 2**23 - 1
        self.cpu.add(5)
        self.cpu.check_overflow(self.cpu.accumulator)
        self.assertEqual(self.cpu.accumulator, -2**23)
        self.output_function.assert_any_call("Added value from memory location 5, new accumulator value: -8388608")

    def test_execute_instruction_read(self):
        self.output_function.return_value = '1234'
        self.cpu.execute_instruction(100007)
        self.memory.write.assert_called_with(7, 1234)

    def test_execute_instruction_write(self):
        self.memory.read.return_value = 4321
        self.cpu.execute_instruction(110007)
        self.output_function.assert_any_call("Executed write (opcode 11) on memory location 7: 4321", is_user_output=True)

    def test_execute_instruction_invalid_operand(self):
        self.assertTrue(self.cpu.execute_instruction(100250))
        self.output_function.assert_any_call("Error: Invalid operand 250")

if __name__ == '__main__':
    unittest.main()
