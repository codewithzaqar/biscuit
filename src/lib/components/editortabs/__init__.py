import tkinter as tk

from .tabs import EditorTabs
from ..placeholders.emptytab import EmptyTab


class EditorTabsPane(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tabs = EditorTabs(self)
        self.emptytab = EmptyTab(self)

        # Initially show the tabs notebook (logic to swap to emptytab will come later)
        self.tabs.grid(row=0, column=0, sticky=tk.NSEW)
