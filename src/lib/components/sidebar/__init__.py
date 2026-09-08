import tkinter as tk


class Sidebar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        # NEW: Clean white background for the sidebar frame
        self.config(width=50, bg='#FFFFFF', relief=tk.FLAT, borderwidth=2)

        # UPDATED: Uniform light gray buttons with dark text and hover states
        btn_style = dict(
            height=3, width=6, relief=tk.FLAT, font=("Consolas", 10), 
            bg="#DEDDDD", fg="#000000", 
            activebackground="#A9A9A9", activeforeground="#45494c"
        )

        btn1 = tk.Menubutton(self, text="A", **btn_style)
        btn1.pack(fill=tk.X, side=tk.TOP)
        
        btn2 = tk.Menubutton(self, text="B", **btn_style)
        btn2.pack(fill=tk.X, side=tk.TOP)
        
        btn3 = tk.Menubutton(self, text="C", **btn_style)
        btn3.pack(fill=tk.X, side=tk.TOP)
        
        btn4 = tk.Menubutton(self, text="D", **btn_style)
        btn4.pack(fill=tk.X, side=tk.TOP)
        
        btn5 = tk.Menubutton(self, text="E", **btn_style)
        btn5.pack(fill=tk.X, side=tk.TOP)

        # NEW: 6th button anchored to the bottom (usually for Settings/Gear icon)
        btn6 = tk.Menubutton(self, text="F", **btn_style)
        btn6.pack(fill=tk.X, side=tk.BOTTOM)
