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

    def fill_tree(self, node):
        for item in self.get_children(node):
            self.delete(item)

        path = self.set(node, "fullpath")

        for p in sorted(os.listdir(path)):
            p_path = os.path.join(path, p)
            ptype = "directory" if os.path.isdir(p_path) else "file"

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
        dfpath = os.path.abspath(os.path.expanduser(startpath))
        root_id = self.insert(
            "", 'end', 
            text=dfpath, 
            values=[dfpath, "directory"], 
            open=True
        )
        self.fill_tree(self.get_children()[0])
