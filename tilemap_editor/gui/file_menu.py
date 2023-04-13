import thorpy
from ..io import map_loader

def create(width):
    opened_file_text    = thorpy.make_text("Currently opened file:\n" + map_loader.current_file)
    opened_file_text.scale_to_title()
    files_box           = thorpy.Box(elements=[opened_file_text])
    files_box.fit_children()
    height = files_box.get_size()[1]
    files_box.set_size((width, height))
    return files_box