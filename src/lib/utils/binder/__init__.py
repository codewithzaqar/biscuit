from lib.config.bindings import Bindings


class Binder:
    def __init__(self, base, *args, **kwargs):
        self.base = base
        self.root = self.base.root
        self.bindings = self.base.bindings

        # MUST be bind_all(), not bind()
        self.bind_all()

    def bind_all(self):
        # Each of these calls bind() with TWO arguments
        self.bind('<Control-n>', self.base.newfile)
        self.bind('<Control-N>', self.base.newwindow)
        self.bind('<Control-o>', self.base.openfile)
        self.bind('<Control-O>', self.base.opendir)
        self.bind('<Control-s>', self.base.save)
        self.bind('<Control-S>', self.base.saveas)
        self.bind('<Control-w>', self.base.closefile)
        self.bind('<Control-q>', self.base.exit)

    def bind(self, this, to_this):
        self.root.bind(this, to_this)
