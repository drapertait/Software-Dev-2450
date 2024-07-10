import tkinter as tk
from tkinter import colorchooser
import configparser

def load_color_scheme():
    config = configparser.ConfigParser()
    config.read('config.txt')
    primary_color = config['DEFAULT'].get('primary_color', '#4C721D')
    off_color = config['DEFAULT'].get('off_color', '#FFFFFF')
    return primary_color, off_color

def apply_color_scheme(root, text_area, primary_color, off_color):
    root.configure(bg=primary_color)
    text_area.configure(bg=off_color)

def set_color_scheme(root, text_area, config):
    primary_color = colorchooser.askcolor(title="Choose Primary Color")[1]
    off_color = colorchooser.askcolor(title="Choose Off Color")[1]
    if primary_color and off_color:
        apply_color_scheme(root, text_area, primary_color, off_color)
        save_color_scheme(config, primary_color, off_color)

def save_color_scheme(config, primary_color, off_color):
    config['DEFAULT']['primary_color'] = primary_color
    config['DEFAULT']['off_color'] = off_color
    with open('config.txt', 'w') as configfile:
        config.write(configfile)
