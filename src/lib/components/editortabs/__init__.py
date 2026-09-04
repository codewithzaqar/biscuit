import os
from tkinter import ttk

from ..editor import Editor


class EditorTabs(ttk.Notebook):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        # dnd
        self.configure(ondrop=self.drop)

        # NEW: Cache for closed tabs to preserve state
        self.closed_tabs = {}
        # {path: [name, exists, editor]}

        self.opened_editors = {}
        # {path: [name, exists, editor]}

        # NEW: Sync Base.active_file when user clicks a different tab
        self.bind("<<NotebookTabChanged>>", self.refresh_active_file)

    def drop(self, event):
        if os.path.isfile(event.data):
            self.base.set_active_tab(file=event.data, exists=True)
        elif os.path.isdir(event.data):
            self.base.open_in_new_window(dir=event.data)

        self.base.trace(f"Dropped file: {event.data}")

    # NEW: Handles tab switching
    def refresh_active_file(self, e=None):
        self.base.active_file = None
        for editor in self.opened_editors.items():
            if self.index(editor[1][2]) == self.index(self.select()):
                self.base.active_file = editor[0]
                self.base.update_statusbar_ln_col_info()

                self.base.trace(f"Active tab was changed to {editor[0]}")
                break

        self.base.trace(f"Currently Active file: {self.base.active_file}")

    # REFACTORED: Merged update_opened_editors directly into update_tabs
    def update_tabs(self):
        for opened_file in self.base.opened_files:
            filename = os.path.basename(opened_file[0])
            if opened_file[0] not in self.opened_editors.keys() or not opened_file[1]:
                self.add_editor(filename, opened_file[1], opened_file[0])
                self.base.trace(f"Tab<{opened_file}> was added.")

        self.base.trace(f"Opened Tabs {self.opened_editors}")

    def update_opened_editors(self):
        for path, data in self.opened_tabs_data.items():
            if path not in self.opened_editors.keys() or not data[1]:
                self.add_editor(data[0], data[1], path)
        self.base.trace(f"Opened editors {self.opened_editors.keys()}")

    # REFACTORED: Now checks closed_tabs cache before creating a new Editor
    def add_editor(self, name, exists, path):
        if not path in self.closed_tabs.keys():
            self.opened_editors[path] = [name, exists, Editor(self, path, exists)]
            self.opened_editors[path][2].configure(height=25, width=75)
            self.add(self.opened_editors[path][2], text=name)
        else:
            # Restore from cache!
            self.opened_editors[path] = self.closed_tabs.pop(path)
            self.opened_editors[path][2].configure(height=25, width=75)
            self.add(self.opened_editors[path][2], text=name)

        # NEW: switch to newly added tab
        self.select(self.opened_editors[path][2])

        self.base.trace(f"Editor<{path}> was added.")

    def set_active_tab(self, path):
        if path in self.opened_tabs_data.keys():
            self.select(self.opened_editors[path][2])
        else:
            self.base.trace(f"Tab<{path}> was not found.")

    def close_active_tab(self):
        for item in self.winfo_children():
            if str(item) == self.select():
                item.destroy()
                break

    def get_active_tab(self):
        return self.opened_editors[self.base.active_file][2]

    def get_active_text(self):
        return self.opened_editors[self.base.active_file][2].text.get_all_text()

    # REPLACES close_active_tab: Hides the tab instead of destroying it
    def remove_tab(self, tab):
        if not tab:
            return

        self.closed_tabs[tab] = self.opened_editors[tab]
        self.hide(self.opened_editors[tab][2])

        self.opened_editors.pop(tab)
        self.update_tabs()
        self.refresh_active_file()

        self.base.trace(f"Active tab was closed. \nClosed Tabs: {self.closed_tabs}")
