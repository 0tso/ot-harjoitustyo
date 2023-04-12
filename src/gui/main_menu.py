import thorpy
from . import manager, file_menu, tile_menu

menu_functions  = [file_menu.create, tile_menu.create]
menu_boxes      = [None, None]

# position as from the top left corner
MAIN_VIEW_POSITION = (10, 10)

active_menu = 2 # 0 = file, 1 = tile, 2 = minimized

def update_menu():
    global menu_box

    thorpy.store(menu_box, mode="v", gap=5, align="left")
    menu_box.fit_children()

def open_menu(id: int):
    global menu_box, active_menu

    if active_menu == id:
        return
    
    minimize()
    active_menu = id

    width = menu_box.get_size()[0] - manager.DEFAULT_MARGIN * 2
    box = menu_functions[id](width)
    menu_boxes[id] = box
    menu_box.add_element(box)
    update_menu()

def minimize():
    global active_menu, menu_box

    if active_menu == 2:
        return
    
    menu_box.remove_elements([menu_boxes[active_menu]])
    
    active_menu = 2
    update_menu()

def create():
    global menu_box

    file_menu_button    = thorpy.make_button("File", func=open_menu, params={"id": 0})
    tile_menu_button    = thorpy.make_button("Tiles", func=open_menu, params={"id": 1})
    minimize_button     = thorpy.make_button("Minimize", func=minimize)
    menu_buttons_group  = thorpy.make_group([file_menu_button, tile_menu_button, minimize_button], mode="h")

    menu_box = thorpy.Box(elements=[menu_buttons_group])
    update_menu()
    menu_box.set_topleft(MAIN_VIEW_POSITION)
    return menu_box