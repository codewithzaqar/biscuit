import time

from .button import SButton

class SClock(SButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update()

    def update(self):
        time_live = time.strftime("%H:%M:%S")
        self.config(text=time_live)
        # Schedule the next update in 200ms
        self.after(200, self.update)
