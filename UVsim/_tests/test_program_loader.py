import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import pytest
from program_loader_class import ProgramLoader

def test_load_program_from_file(tmp_path):
    program_content = "1000\n2000\n3000\n"
    file_path = tmp_path / "program.txt"
    file_path.write_text(program_content)
    
    program = ProgramLoader.load_program_from_file(file_path)
    assert program == [1000, 2000, 3000]

def test_load_program_exceeds_limit(tmp_path):
    program_content = "\n".join("1000" for _ in range(251))
    file_path = tmp_path / "program.txt"
    file_path.write_text(program_content)
    
    with pytest.raises(ValueError, match="Program exceeds the maximum allowed size of 250 commands."):
        ProgramLoader.load_program_from_file(file_path)
