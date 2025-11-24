import tkinter as tk
print("tkinter imported, version:", tk.TkVersion)
root = tk.Tk()
root.title("TK Test - will close in 2s")
root.geometry("300x80")
root.after(2000, root.destroy)   # auto close after 2 seconds
root.mainloop()
print("tkinter test finished")
