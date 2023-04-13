import thorpy
import tkinter
import tkinter.filedialog
from ..io import map_loader

def open_file_browser():
    tk = tkinter.Tk()
    tk.withdraw()
    file_path = tkinter.filedialog.askopenfilename(parent=tk)
    tk.destroy()
    map_loader.load_from_path(file_path)
    opened_text.set_text("File: " + map_loader.current_file_name)
    opened_text.scale_to_text()

def create(width):
    global opened_text

    opened_text         = thorpy.make_text("File: " + map_loader.current_file_name)
    browse_files_button = thorpy.make_button("Browse files", func=open_file_browser)

    files_box           = thorpy.Box(elements=[opened_text, browse_files_button])
    files_box.fit_children()
    files_box.set_size((width, None))

    return files_box