import thorpy

# position as from the top left corner
MAIN_VIEW_POSITION = (10, 10)

def open_file_menu():
    pass

def open_tile_menu():
    pass

def minimize():
    pass

def create():
    file_menu_button    = thorpy.make_button("File", func=open_file_menu)
    tile_menu_button    = thorpy.make_button("Tiles", func=open_tile_menu)
    minimize_button     = thorpy.make_button("Minimize", func=minimize)
    box = thorpy.Box(elements=[file_menu_button, tile_menu_button, minimize_button])
    thorpy.store(box, mode="h", gap=10, align="top")
    box.fit_children((5, 5))
    box.set_topleft(MAIN_VIEW_POSITION)
    return box