import json, os
import tkinter as tk


class ResourcesLoader:
    def __init__(self, master):
        self.base = master.base

    def load_image(self, resource):
        path = self.base.get_res_path(resource)
        try:
            return tk.PhotoImage(file=path)
        except tk.TclError:
            # Fallback: return a blank 1x1 transparent pixel if the file is missing
            self.base.trace(f"Warning: Resources '{resource}' not found at {path}. Using blank fallback.")
            return tk.PhotoImage(width=1, height=1)
