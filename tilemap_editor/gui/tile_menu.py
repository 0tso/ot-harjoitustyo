import thorpy

def create(width):
    no_tiles_text   = thorpy.make_text("No tiles available.")
    tiles_box       = thorpy.Box(elements=[no_tiles_text])
    tiles_box.fit_children()
    tiles_box.set_size((width, None))
    return tiles_box