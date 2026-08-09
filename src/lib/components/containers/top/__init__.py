import tkinter as tk

from lib.components.containers.top.left import TopLeftPane
from lib.components.containers.top.right import TopRightPane

class TopPane(tk.PanedWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.left = TopLeftPane(self, width=290)
        self.right = TopRightPane(self, width=990)

        self.add(self.left)
        self.add(self.right)
