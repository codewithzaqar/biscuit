import os
import tkinter.ttk as ttk


class DirTree(ttk.Treeview):
    def __init__(self, master, startpath, *args, **kwargs):
        kwargs.setdefault('columns', ("fullpath", "type"))
        kwargs.setdefault('show', "tree")
        super().__init__(master, *args, **kwargs)
        self.heading('#0', text='Directory', anchor='w')
        self.column('#0', anchor='w', width=250)

        self.column("fullpath", width=0, stretch=False)
        self.column("type", width=0, stretch=False)

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
        root_node = self.get_children()[0]
        self.fill_tree(root_node)
