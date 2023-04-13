import thorpy
from ..io import tileset_loader
from . import file_browser

def open_file_browser():
    dir_path = file_browser.open(directory=True)
    tileset_loader.load(dir_path)
    dir_text.set_text("Directory:\n" + ".." + tileset_loader.current_dir_path[-20:])
    dir_text.scale_to_title()
    tiles_box.fit_children()


def create(width):
    global dir_text, tiles_box

    dir_text            = thorpy.make_text("Directory:\n" + ".." + tileset_loader.current_dir_path[-20:])
    browse_dirs_button  = thorpy.make_button("Browse directories", func=open_file_browser)
    
    tiles_box       = thorpy.Box(elements=[dir_text, browse_dirs_button])
    tiles_box.fit_children()
    tiles_box.set_size((width, None))
    return tiles_box