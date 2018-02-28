import tkinter as tk
import os  

def write_slogan():
    os.system("eject.bat")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

slogan = tk.Button(frame,
                   text="cup holder",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
