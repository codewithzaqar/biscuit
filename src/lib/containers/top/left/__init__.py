import tkinter as tk

from lib.components.dirtree import DirTree

class TopLeftPane(tk.PanedWindow):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        # NEW: Stack children vertically
        self.config(orient=tk.VERTICAL)

        # NEW: Add a static header label
        self.label = tk.Label(self, text="Explorer", anchor=tk.W)
        self.add(self.label, pady=2, padx=5)

        self.dirtree = DirTree(self, '.')
        self.dirtree.configure(height=25)
        self.add(self.dirtree)
