import tkinter as tk

from .left import LeftPane
from .right import RightPane


class BasePane(tk.PanedWindow):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        self.configure(orient=tk.HORIZONTAL)

        self.left = LeftPane(self)
        self.right = RightPane(self)

        self.add(self.left)
        self.add(self.right)
