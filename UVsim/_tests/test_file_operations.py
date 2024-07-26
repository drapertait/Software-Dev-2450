import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
import tkinter as tk
from unittest.mock import Mock, patch, mock_open
from file_operations import open_file, save_file, save_file_as

@pytest.fixture
def text_area():
    root = tk.Tk()
    text = tk.Text(root)
    yield text
    root.destroy()

def test_convert_4bit_to_6bit():
    from file_operations import convert_4bit_to_6bit

    assert convert_4bit_to_6bit("1007") == "010007"
    assert convert_4bit_to_6bit("5555") == "005555"
    assert convert_4bit_to_6bit("1234") == "001234"

@patch("file_operations.filedialog.askopenfilename")
def test_open_file(mock_askopenfilename, text_area):
    mock_askopenfilename.return_value = "test_program.txt"
    with patch("builtins.open", mock_open(read_data="1000\n2000\n")) as mock_file:
        open_file(text_area)
        mock_file.assert_called_once_with("test_program.txt", "r")
        assert text_area.get("1.0", tk.END).strip() == "010000\n020000"

@patch("file_operations.filedialog.asksaveasfilename")
def test_save_file_as(mock_asksaveasfilename, text_area):
    mock_asksaveasfilename.return_value = "test_program.txt"
    text_area.insert("1.0", "010000\n020000\n")
    with patch("builtins.open", mock_open()) as mock_file:
        save_file_as(text_area)
        mock_file.assert_called_once_with("test_program.txt", "w")
        mock_file().write.assert_called_once_with("010000\n020000")

@patch("file_operations.filedialog.asksaveasfilename")
def test_save_file(mock_asksaveasfilename, text_area):
    current_file = "test_program.txt"
    text_area.insert("1.0", "010000\n020000\n")
    with patch("builtins.open", mock_open()) as mock_file:
        save_file(text_area, current_file)
        mock_file.assert_called_once_with(current_file, "w")
        mock_file().write.assert_called_once_with("010000\n020000")
