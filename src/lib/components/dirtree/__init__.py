import tkinter as tk

from ..sidebar.pane import SidePane
from .tree import DirTreeTree
from ..utils.scrollbar import AutoScrollbar


class DirTreePane(SidePane):
    def __init__(self, master, before=None, *args, **kwargs):
        super().__init__(master, before=before, *args, **kwargs)
        self.base = master.base 

        # Allow the tree to expand and fill the frame
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label = tk.Label(self, text="Explorer", anchor=tk.W, padx=10, pady=10)
        self.label.grid(row=0, column=0, sticky=tk.EW)

        # Initialize the actual tree widget
        self.tree = DirTreeTree(self, selectmode=tk.BROWSE)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        # Initialize the auto-hiding scrollbar and link it to the tree
        self.tree_scrollbar = AutoScrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree_scrollbar.grid(row=1, column=1, sticky=tk.NS)

        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)

    def create_root(self, startpath):
        self.tree.create_root(startpath)

    def set_heading(self, text):
        self.tree.set_heading(text)

    def openfile(self, event):
        self.tree.openfile(event)
