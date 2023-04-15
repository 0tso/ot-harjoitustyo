import tkinter
import tkinter.filedialog

def open(directory=False):
    tk = tkinter.Tk()
    tk.withdraw()
    path = None
    if directory:
        path = tkinter.filedialog.askdirectory(parent=tk)
    else:
        path = tkinter.filedialog.askopenfilename(parent=tk)
    tk.destroy()
    return path
