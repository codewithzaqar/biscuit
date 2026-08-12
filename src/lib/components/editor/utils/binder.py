from lib.config.bindings import Bindings


class Binder:
    def __init__(self, master, bindings=None):
        self.base = master.base
        self.master = master
    
    def bind_all(self):
        self.master.text.bind("<Control-MouseWheel>", self.master.handle_zoom)
        self.master.text.bind("<<Change>>", self.master._on_change)
        self.master.text.bind("<Configure>", self.master._on_change)
