import tkinter as tk

from .content import EditorContent
from .utils.path import Path


class Editor(tk.Frame):
    def __init__(self, master, path=None, exists=True, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base
        self.master = master

        self.path = path
        self.exists = exists

        # Initialize the top path bar and the bottom content area
        self.pathbar = Path(master=self, text=path)
        self.content = EditorContent(self, path=path, exists=exists)

        # Layout: Path on top (row 0), Content on bottom (row 1, expanding)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.pathbar.grid(row=0, column=0, sticky=tk.EW)
        self.content.grid(row=1, column=0, sticky=tk.NSEW)

    def focus(self):
        self.content.text.focus_set()
