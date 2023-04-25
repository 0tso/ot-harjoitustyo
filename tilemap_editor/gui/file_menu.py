import thorpy
from . import file_browser
from ..data import view


def open_file_browser():
    file_path = file_browser.open()
    if file_path:
        view.load_map(file_path)
        opened_text.set_text("File: " + view.get_current_map_name())

def save_file():
    file_path = file_browser.open(save=True)
    if file_path:
        view.save_map_to_path(file_path)


def create(menu_width):
    global opened_text, saved_changes_text

    opened_text = thorpy.make_text("File: " + view.get_current_map_name())
    browse_files_button = thorpy.make_button(
        "Browse files", func=open_file_browser)
    
    saved_changes_text = thorpy.make_text("No changes")
    save_button = thorpy.make_button("Save", func=save_file)

    files_box = thorpy.Box(elements=[opened_text, browse_files_button, saved_changes_text, save_button])
    files_box.fit_children()
    files_box.set_size((menu_width, None))

    return files_box
