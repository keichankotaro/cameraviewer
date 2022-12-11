# -*- coding:utf-8 -*-
# Copyright (c) 2022 Keichan Kotaro. All Rights Reserved.

import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
import sys
try:
    def apply(root, width, height, x, y, fps, camid):
        with open("./main.cfg", "w") as f:
            f.write(str(width+"|"+height+"|"+x+"|"+y+"|"+fps+"|"+camid))
            f.close()
        messagebox.showinfo("Done!", "Wrote config.")
        root.destroy()
        sys.exit()

    def cancel(root):
        messagebox.showinfo("Exit", "Bye.")
        root.destroy()
        sys.exit()

    with open("./main.cfg", "r") as f:
        cfg = f.readline()
        f.close()

    cfg = cfg.split("|")

    root = tk.Tk()
    root.geometry("200x325")
    br = ttk.Label(text="")

    label1 = ttk.Label(text="width")
    label1.pack()

    textbox1 = ttk.Entry(width=5)
    textbox1.insert(0, cfg[0])
    textbox1.pack()


    label2 = ttk.Label(text="height")
    label2.pack()

    textbox2 = ttk.Entry(width=5)
    textbox2.insert(0, cfg[1])
    textbox2.pack()


    label3 = ttk.Label(text="x")
    label3.pack()

    textbox3 = ttk.Entry(width=5)
    textbox3.insert(0, cfg[2])
    textbox3.pack()


    label4 = ttk.Label(text="y")
    label4.pack()

    textbox4 = ttk.Entry(width=5)
    textbox4.insert(0, cfg[3])
    textbox4.pack()


    label5 = ttk.Label(text="fps")
    label5.pack()

    textbox5 = ttk.Entry(width=5)
    textbox5.insert(0, cfg[4])
    textbox5.pack()
    
    label6 = ttk.Label(text="Device ID")
    label6.pack()

    textbox6 = ttk.Entry(width=5)
    textbox6.insert(0, cfg[5])
    textbox6.pack()

    br.pack()
    btn = ttk.Button(text="Apply", command=lambda:apply(root, textbox1.get(), textbox2.get(), textbox3.get(), textbox4.get(), textbox5.get(), textbox6.get()))
    btn.pack()
    btn2 = ttk.Button(text="Cancel", command=lambda:cancel(root))
    btn2.pack()
    root.mainloop()
    root.lift()
except FileNotFoundError:
    print("Error: Config file (./main.cfg) is not found.")
    raise FileNotFoundError("Config file (./main.cfg) is not found.")
    sys.exit()
except IndexError:
    print("Error: Config file is broaken.")
    root.destroy()
    raise IndexError("Config file (./main.cfg) is broken.")
    sys.exit()
