import tkinter as tk
import tkinter.ttk as ttk

from .tree import DirTreeTree
from ..utils.scrollbar import AutoScrollbar


class DirTree(tk.Frame):
    def __init__(self, master, startpath=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        # Allow the tree to expand and fill the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialize the actual tree widget
        self.tree = DirTreeTree(self, startpath=startpath)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        # Initialize the auto-hiding scrollbar and link it to the tree
        self.scrollbar = AutoScrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

    def create_root(self, startpath):
        self.tree.create_root(startpath)

    def set_heading(self, text):
        self.tree.set_heading(text)

    def openfile(self, event):
        self.tree.openfile(event)
