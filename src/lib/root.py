import os
import tkinter as tk
from tkinterDnD import Tk

from lib.base import Base
from lib.containers import BasePane
from lib.components.statusbar import StatusBar
from lib.components.sidebar import Sidebar


class Root(Tk):
    def __init__(self, path, dir=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.appdir = os.path.dirname(path)

        self.minsize(1290, 800)
        self.title("Biscuit")

        self.base = Base(root=self)

        self.basepane = BasePane(master=self)
        self.basepane.pack(fill=tk.BOTH, expand=1)

        self.statusbar = StatusBar(master=self)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        if dir:
            self.base.set_active_file(dir)

    def run(self):
        self.mainloop()
