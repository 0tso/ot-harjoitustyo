import thorpy
from . import file_browser
from ..io import map_loader

def open_file_browser(directory=False):
    file_path = file_browser.open()
    if file_path:
        map_loader.load_from_path(file_path)
        opened_text.set_text("File: " + map_loader.current_file_name)

def create(menu_width):
    global opened_text

    opened_text         = thorpy.make_text("File: " + map_loader.current_file_name)
    browse_files_button = thorpy.make_button("Browse files", func=open_file_browser)

    files_box           = thorpy.Box(elements=[opened_text, browse_files_button])
    files_box.fit_children()
    files_box.set_size((menu_width, None))

    return files_box