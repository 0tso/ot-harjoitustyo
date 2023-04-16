import thorpy
from . import file_browser
from ..data import view


def open_file_browser():
    file_path = file_browser.open()
    if file_path:
        view.load_map(file_path)
        opened_text.set_text("File: " + view.get_current_map_name())


def create(menu_width):
    global opened_text

    opened_text = thorpy.make_text("File: " + view.get_current_map_name())
    browse_files_button = thorpy.make_button(
        "Browse files", func=open_file_browser)

    files_box = thorpy.Box(elements=[opened_text, browse_files_button])
    files_box.fit_children()
    files_box.set_size((menu_width, None))

    return files_box
