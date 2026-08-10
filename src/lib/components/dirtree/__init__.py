import os
import tkinter.ttk as ttk
import tkinter as tk


class DirTree(ttk.Treeview):
    def __init__(self, master, startpath, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        self.configure(columns=("fullpath", "type"), displaycolumns='')
        self.heading('#0', text="Explorer", anchor=tk.W)

        self.create_root(startpath)

        self.bind("<<TreeviewOpen>>", self.update_tree)
        # self.bind("<<TreeviewSelect>>", self.update_tree)
        self.bind('<Double-Button-1>', self.openfile)

    def openfile(self, event):
        self = event.widget
        item = self.focus()
        # Changed from: if self.set(item, "type") == 'directory'
        if self.set(item, "type") != 'file':
            return
        path = self.set(item, "fullpath")
        self.base.set_active_file(path)

    def fill_tree(self, node):
        if self.set(node, "type") != 'directory':
            return

        for item in self.get_children(node):
            self.delete(item)

        path = self.set(node, "fullpath")

        for p in sorted(os.listdir(path)):
            p_path = os.path.join(path, p)

            # Explicit type detection
            ptype = None
            if os.path.isdir(p_path):
                ptype = 'directory'
            elif os.path.isfile(p_path):
                ptype = 'file' 

            oid = self.insert(
                node, "end", 
                text=p, 
                values=[p_path, ptype], 
                open=False
            )

            if ptype == "directory":
                self.insert(oid, 0, text="dummy")

    def update_tree(self, event):
        self.fill_tree(self.focus())

    def create_root(self, startpath):
        # NEW: clear existing items before rebuilding
        self.delete(*self.get_children())
        dfpath = os.path.abspath(startpath)
        node = self.insert(
            "", 'end', 
            text=dfpath, 
            values=[dfpath, "directory"], 
            open=True
        )
        self.fill_tree(node)
