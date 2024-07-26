import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from memory_class import Memory

@pytest.fixture
def memory():
    return Memory()

def test_memory_read(memory):
    memory.write(10, 1234)
    assert memory.read(10) == 1234

def test_memory_write(memory):
    memory.write(10, 4321)
    assert memory.read(10) == 4321

def test_memory_reset(memory):
    memory.write(10, 1234)
    memory.reset()
    assert memory.read(10) == 0

def test_memory_str(memory):
    memory.write(0, 123456)
    memory.write(1, 654321)
    memory_str = str(memory)
    assert "000: 123456" in memory_str
    assert "001: 654321" in memory_str
