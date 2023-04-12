import thorpy

def create(width):
    placeholder_text    = thorpy.make_text("Placeholder text")
    files_box           = thorpy.Box(elements=[placeholder_text])
    files_box.fit_children()
    height = files_box.get_size()[1]
    files_box.set_size((width, height))
    return files_box