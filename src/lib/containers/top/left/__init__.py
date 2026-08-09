import tkinter as tk

from lib.components.editor import Editor

class TopLeftPane(tk.PanedWindow):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        self.editor = Editor(self)          # ← pane as master, not self.base
        self.editor.configure(height=25, width=25)
        self.add(self.editor)
