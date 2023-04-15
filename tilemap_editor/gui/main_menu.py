import thorpy
from . import manager

menu_functions  = []
menu_boxes      = []

# position as from the top left corner
MAIN_VIEW_POSITION = (10, 10)

active_menu = 2 # 0 = file, 1 = tile, 2 = minimized

def reload():
    open_menu(active_menu)

def update_menu():
    global menu_box

    thorpy.store(menu_box, mode="v", gap=5, align="left", margin=5)
    menu_box.fit_children()

def open_menu(id: int):
    global menu_box, active_menu
    
    minimize()
    active_menu = id

    width = menu_box.get_size()[0] - 10
    box = menu_functions[id](width)
    menu_boxes[id] = box
    menu_box.add_element(box)
    manager.add_element(box)
    update_menu()

def minimize():
    global active_menu, menu_box

    if active_menu == 2:
        return
    
    element = menu_boxes[active_menu]
    menu_box.remove_elements([element])
    manager.remove_element(element)
    
    active_menu = 2
    update_menu()

# list format: [(name, function), ...]
def create(menus: list):
    global menu_box, menu_functions, menu_boxes

    menu_functions = [function for name, function in menus]
    menu_buttons = [thorpy.make_button(name, func=open_menu, params={"id": i}) for i, (name, function) in enumerate(menus)]
    menu_boxes = [None] * len(menus)
    minimize_button     = thorpy.make_button("Minimize", func=minimize)
    menu_buttons_group  = thorpy.make_group(menu_buttons + [minimize_button], mode="h")

    menu_box = thorpy.Box(elements=[menu_buttons_group])
    update_menu()
    menu_box.set_topleft(MAIN_VIEW_POSITION)
    return menu_box