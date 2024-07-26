import pytest
from unittest.mock import Mock
from cpu_class import CPU

@pytest.fixture
def cpu():
    memory = Mock()
    output_function = Mock()
    return CPU(memory, output_function)

def test_read(cpu):
    cpu.output_function.return_value = '1234'
    cpu.read(7)
    cpu.memory.write.assert_called_with(7, 1234)
    cpu.output_function.assert_any_call("Executed read (opcode 010) on memory location 007: 1234", is_user_output=True)

def test_write(cpu):
    cpu.memory.read.return_value = 4321
    cpu.write(7)
    cpu.output_function.assert_any_call("Executed write (opcode 011) on memory location 007: 4321", is_user_output=True)

def test_load(cpu):
    cpu.memory.read.return_value = 1000
    cpu.load(10)
    assert cpu.accumulator == 1000
    cpu.output_function.assert_any_call("Loaded value 1000 from memory location 010 into accumulator.")

def test_store(cpu):
    cpu.accumulator = 2000
    cpu.store(10)
    cpu.memory.write.assert_called_with(10, 2000)
    cpu.output_function.assert_any_call("Stored value 2000 from accumulator into memory location 010.")

def test_add(cpu):
    cpu.memory.read.return_value = 3000
    cpu.accumulator = 2000
    cpu.add(5)
    assert cpu.accumulator == 5000
    cpu.output_function.assert_any_call("Added value from memory location 005, new accumulator value: 5000")

def test_subtract(cpu):
    cpu.memory.read.return_value = 1000
    cpu.accumulator = 2000
    cpu.subtract(5)
    assert cpu.accumulator == 1000
    cpu.output_function.assert_any_call("Subtracted value from memory location 005, new accumulator value: 1000")

def test_divide(cpu):
    cpu.memory.read.return_value = 2
    cpu.accumulator = 10
    cpu.divide(5)
    assert cpu.accumulator == 5
    cpu.output_function.assert_any_call("Divided by value from memory location 005, new accumulator value: 5")

def test_divide_by_zero(cpu):
    cpu.memory.read.return_value = 0
    cpu.accumulator = 10
    cpu.divide(5)
    cpu.output_function.assert_any_call("Error: Division by zero")

def test_multiply(cpu):
    cpu.memory.read.return_value = 3
    cpu.accumulator = 4
    cpu.multiply(5)
    assert cpu.accumulator == 12
    cpu.output_function.assert_any_call("Multiplied by value from memory location 005, new accumulator value: 12")

def test_branch(cpu):
    cpu.branch(20)
    assert cpu.instruction_counter == 20

def test_branchneg(cpu):
    cpu.accumulator = -10
    cpu.branchneg(15)
    assert cpu.instruction_counter == 15

def test_branchneg_no_jump(cpu):
    cpu.accumulator = 10
    cpu.branchneg(15)
    assert cpu.instruction_counter != 15

def test_branchzero(cpu):
    cpu.accumulator = 0
    cpu.branchzero(10)
    assert cpu.instruction_counter == 10

def test_branchzero_no_jump(cpu):
    cpu.accumulator = 5
    cpu.branchzero(10)
    assert cpu.instruction_counter != 10

def test_halt(cpu):
    assert cpu.halt() is True
    cpu.output_function.assert_any_call("Program encountered halt (043) opcode.")

def test_overflow(cpu):
    cpu.memory.read.return_value = 5
    cpu.accumulator = 9999
    cpu.add(5)
    assert cpu.accumulator == -9994  # Adjusted based on new overflow logic
    cpu.output_function.assert_any_call("Added value from memory location 005, new accumulator value: -9994")

def test_execute_instruction_read(cpu):
    cpu.output_function.return_value = '1234'
    cpu.execute_instruction(100007)
    cpu.memory.write.assert_called_with(7, 1234)

def test_execute_instruction_write(cpu):
    cpu.memory.read.return_value = 4321
    cpu.execute_instruction(110007)
    cpu.output_function.assert_any_call("Executed write (opcode 011) on memory location 007: 4321", is_user_output=True)

def test_execute_instruction_invalid_operand(cpu):
    assert cpu.execute_instruction(100250) is True
    cpu.output_function.assert_any_call("Error: Invalid operand 250")
