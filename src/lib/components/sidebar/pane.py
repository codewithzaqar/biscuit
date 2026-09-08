import tkinter as tk


class SidePane(tk.Frame):
    def __init__(self, master, before=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.active = False

        # Store the refernce to the pane that should always be to the right of this one
        self.before = before

    def toggle(self):
        self.active = not self.active

        if self.active:
            # Re-adds the pane exactly where it was originally
            self.master.add(self, before=self.before)
        else:
            # Removes the pane from the PanedWindow layout
            self.master.forget(self)
