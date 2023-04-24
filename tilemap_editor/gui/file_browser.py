import tkinter
import tkinter.filedialog


def open(directory=False, save=False):
    tk = tkinter.Tk()
    tk.withdraw()
    path = None
    if save:
        path = tkinter.filedialog.asksaveasfilename(parent=tk)
    elif directory:
        path = tkinter.filedialog.askdirectory(parent=tk)
    else:
        path = tkinter.filedialog.askopenfilename(parent=tk)
    tk.destroy()
    return path