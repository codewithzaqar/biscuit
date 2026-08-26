import subprocess, os, sys
import tkinter as tk
import tkinter.filedialog as filedialog

from datetime import datetime

from lib.settings import Settings
from lib.utils.events import Events
from lib.utils.binder import Binder

class Base:
    def __init__(self, root, *args, **kwargs):
        self.root = root
        self.appdir = root.appdir
        self.settings = Settings(self)
        self.bindings = self.settings.bindings

        self.active_dir = None
        self.active_file = None

        # Opened files
        # [file, exists]
        self.opened_files = []

        self.events = Events(self)
        self.binder = Binder(base=self)

    def trace(self, e):
        time = datetime.now().strftime('•%H:%M:%S•')
        print(f'TRACE {time} {e}')

    def refresh_dir(self):
        self.root.basepane.top.left.dirtree.create_root(self.active_dir)

    def set_active_file(self, file, exists=True):
        self.active_file = file
        self.trace(f"Active file<{self.active_file}>")

        if file not in [f[0] for f in self.opened_files]:
            # Removed debug print("❤❤", self.opened_files)
            self.add_to_open_files(file, exists)
            self.trace(f"File<{self.active_file}> was added.")
        else:
            self.root.basepane.top.right.editortabs.set_active_tab(file)

    def set_active_dir(self, dir):
        if not os.path.isdir(dir):
            return

        self.active_dir = dir
        self.refresh_dir()
        self.clean_opened_files()
        self.trace(self.active_dir)

    def add_to_open_files(self, file, exists):
        self.opened_files.append([file, exists])
        self.trace(f"Opened Files {self.opened_files}")

        self.root.basepane.top.right.editortabs.update_tabs()

    def remove_from_open_files(self, file):
        # FIXED: Iterate to find the [path, exists] pair instead of trying to remove a string directly
        for i in self.opened_files:
            if i[0] == file:
                self.opened_files.remove(i)

    def get_opened_files(self):
        return self.opened_files

    def clean_opened_files(self):
        self.opened_files = []
        self.active_file = None
        self.trace(f"<ClearOpenFilesEvent>({self.opened_files})")

    def open_in_new_window(self, dir):
        subprocess.Popen(["python", sys.argv[0], dir])
        self.trace('Opened in new window: {dir}')

    def open_new_window(self):
        subprocess.Popen(["python", sys.argv[0]])
        self.trace(f"Opened new window")

    def update_statusbar_ln_col_info(self):
        if not self.active_file or self.active_file not in self.root.basepane.top.right.editortabs.opened_editors:
            self.root.statusbar.set_line_col_info("?", "?", 0)
            return

        active_text = self.root.basepane.top.right.editortabs.get_active_tab().text
        self.root.statusbar.set_line_col_info(
            active_text.line,
            active_text.column,
            active_text.get_selected_count()
        )
