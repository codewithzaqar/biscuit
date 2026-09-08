import tkinter as tk

root = tk.Tk()
root.geometry("1000x600")

sidebar = tk.Frame(root, width=50, bg='#aa6f73', height=500, relief=tk.FLAT, borderwidth=2)
sidebar.pack(fill='y', side='left', anchor='nw')

# UPDATED: Unified styling and added pady=1 for spacing
btn_style = dict(height=3, width=6, relief=tk.FLAT, font=("Consolas", 10), 
                 bg="#F8B195", fg="#aa6f73", activebackground="#aa6f73", activeforeground="#FFFFFF")

btn1 = tk.Menubutton(sidebar, text="A", **btn_style)
btn1.pack(fill=tk.X, side=tk.TOP, pady=1)
btn2 = tk.Menubutton(sidebar, text="B", **btn_style)
btn2.pack(fill=tk.X, side=tk.TOP, pady=1)
btn3 = tk.Menubutton(sidebar, text="C", **btn_style)
btn3.pack(fill=tk.X, side=tk.TOP, pady=1)
btn4 = tk.Menubutton(sidebar, text="D", **btn_style)
btn4.pack(fill=tk.X, side=tk.TOP, pady=1)
btn5 = tk.Menubutton(sidebar, text="E", **btn_style)
btn5.pack(fill=tk.X, side=tk.TOP, pady=1)

btn6 = tk.Menubutton(sidebar, text="F", **btn_style)
btn6.pack(fill=tk.X, side=tk.BOTTOM)

# REFACTORED: Changed from LeftFrame to LeftPane (inheriting from PanedWindow)
class LeftPane(tk.PanedWindow):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.active = False
        self.pack_data = {}

    def set_pack_data(self, **kwargs):
        self.pack_data = kwargs

    def toggle(self):
        self.active = not self.active

        if self.active:
            # UPDATED: Use stored pack_data instead of paneconfig hacks
            self.master.add(self, **self.pack_data)
        else:
            self.master.forget(self)

# +——+==========+=================+
# |  |          |                 |
# |S |  Left    |                 |
# |i |  Pane    |   Main Area     |
# |d |          |                 |
# |e |          |                 |
# |b |          |                 |
# |a |          |                 |
# |r |          |                 |
# +——+==========+=================+

base = tk.PanedWindow(orient=tk.HORIZONTAL, bd=0)
base.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

# UPDATED: Panes are now added directly to the base PanedWindow
left1 = LeftPane(base, bg='#aa6f73', width=300)
t1 = tk.Label(left1, text="Pane 1", font=("Consolas", 50, "bold"), bg='#aa6f73', fg="#FFFFFF")
left1.add(t1)

left2 = LeftPane(base, bg='#aa6f73', width=300)
t2 = tk.Label(left2, text="Pane 2", font=("Consolas", 50, "bold"), bg='#aa6f73', fg="#FFFFFF")
left2.add(t2)

left3 = LeftPane(base, bg='#aa6f73', width=300)
t3 = tk.Label(left3, text="Pane 3", font=("Consolas", 50, "bold"), bg='#aa6f73', fg="#FFFFFF")
left3.add(t3)

left4 = LeftPane(base, bg='#aa6f73', width=300)
t4 = tk.Label(left4, text="Pane 4", font=("Consolas", 50, "bold"), bg='#aa6f73', fg="#FFFFFF")
left4.add(t4)

left5 = LeftPane(base, bg='#aa6f73', width=300)
t5 = tk.Label(left5, text="Pane 5", font=("Consolas", 50, "bold"), bg='#aa6f73', fg="#FFFFFF")
left5.add(t5)

left_frames = [left1, left2, left3, left4, left5]

# main content area
mainarea = tk.PanedWindow(base, bg='#F8B195')
base.add(mainarea, sticky=tk.NSEW)

main_txt = tk.Text(mainarea, bg='#F8B195', fg="#aa6f73", font=("Consolas", 20), bd=0)
main_txt.pack(expand=True, fill='both', padx=10, pady=10)

# NEW: The "Refresh" hack to force Tkinter to recalculate the layout
def refresh():
    base.forget(mainarea)
    base.add(mainarea, sticky=tk.NSEW)
    print_active()

def remove_all_left_active(frame):
    for i in left_frames:
        if i != frame and i.active:
            i.toggle()

def print_active():
    for i in left_frames:
        if i.active:
            print(f"Active: {i}")

def b1(e):
    remove_all_left_active(left1)
    left1.toggle()
    refresh()
btn1.bind('<Button-1>', b1)

def b2(e):
    remove_all_left_active(left2)
    left2.toggle()
    refresh()
btn2.bind('<Button-1>', b2)

def b3(e):
    remove_all_left_active(left3)
    left3.toggle()
    refresh()
btn3.bind('<Button-1>', b3)

def b4(e):
    remove_all_left_active(left4)
    left4.toggle()
    refresh()
btn4.bind('<Button-1>', b4)

def b5(e):
    remove_all_left_active(left5)
    left5.toggle()
    refresh()
btn5.bind('<Button-1>', b5)

root.mainloop()
