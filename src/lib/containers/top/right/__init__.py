import tkinter as tk

from lib.components.editortabs import EditorTabs
from lib.components.editor import Editor

class TopRightPane(tk.PanedWindow):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        self.editortabs = EditorTabs(self)
        self.editortabs.configure(height=25, width=75)
        self.add(self.editortabs)

        # Add two default tabs with editors
        self.editortabs.add(Editor(self), text="Untitled")
        self.editortabs.add(Editor(self), text="base.py")
