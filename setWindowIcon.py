import os
import sys
import tkinter as tk

def resource_path(relative_path):
    """Trova il percorso reale per dev e PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def set_window_icon(app):
    if sys.platform.startswith("win"):
        app.iconbitmap(resource_path("./data/icons/bug.ico"))
    else:
        icon = tk.PhotoImage(master=app, file=resource_path("./data/icons/bug.png"))
        app.iconphoto(True, icon)