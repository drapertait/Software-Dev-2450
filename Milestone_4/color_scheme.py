import tkinter as tk
from tkinter import colorchooser
import configparser


def load_color_scheme():
    # Always set default color scheme
    primary_color = '#4C721D'
    off_color = '#FFFFFF'
    return primary_color, off_color


def apply_color_scheme(root, primary_color, off_color):
    root.configure(bg=primary_color)
    for widget in root.winfo_children():
        try:
            widget.configure(bg=primary_color)
        except tk.TclError:
            pass
        if 'fg' in widget.keys():
            widget.configure(fg=get_contrasting_color(off_color))
        if isinstance(widget, tk.Text):
            widget.configure(bg=off_color, fg=get_contrasting_color(off_color))
        for subwidget in widget.winfo_children():
            try:
                subwidget.configure(bg=primary_color)
            except tk.TclError:
                pass
            if 'fg' in subwidget.keys():
                subwidget.configure(fg=get_contrasting_color(off_color))
            if isinstance(subwidget, tk.Text):
                subwidget.configure(
                    bg=off_color, fg=get_contrasting_color(off_color))


def get_contrasting_color(color):
    # Convert hex color to RGB
    color = color.lstrip('#')
    r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
    # Calculate luminance
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    # Return black for light colors and white for dark colors
    return '#000000' if luminance > 0.5 else '#FFFFFF'


def set_color_scheme(root, text_area):
    primary_color = colorchooser.askcolor(title="Choose Primary Color")[1]
    off_color = colorchooser.askcolor(title="Choose Off Color")[1]
    if primary_color and off_color:
        apply_color_scheme(root, primary_color, off_color)
        save_color_scheme(primary_color, off_color)


def save_color_scheme(primary_color, off_color):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'primary_color': primary_color,
        'off_color': off_color
    }
    with open('config.txt', 'w') as configfile:
        config.write(configfile)
