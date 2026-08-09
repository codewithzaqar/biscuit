import tkinter as tk

from lib.containers.base.top import TopPane
from lib.containers.base.bottom import BottomPane

class BasePane(tk.PanedWindow):
    def __init__(self):
        super().__init__()
        self.configure(orient=tk.VERTICAL)

        self.top = TopPane(self)
        self.bottom = BottomPane(self)

        self.add(self.top)
        self.add(self.bottom)
