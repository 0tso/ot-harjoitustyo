import thorpy
from . import manager

# position as from the top left corner
MAIN_VIEW_POSITION = (10, 10)

_menu_functions = []
_menu_boxes = []

_active_menu = 2  # 0 = file, 1 = tile, 2 = minimized


def reload():
    open_menu(_active_menu)


def update_menu():
    thorpy.store(menu_box, mode="v", gap=5, align="left", margin=5)
    menu_box.fit_children()


def open_menu(menu_id: int):
    global _active_menu

    minimize()
    _active_menu = menu_id

    width = menu_box.get_size()[0] - 10
    box = _menu_functions[menu_id](width)
    _menu_boxes[menu_id] = box
    menu_box.add_element(box)
    manager.add_element(box)
    update_menu()


def minimize():
    global _active_menu

    if _active_menu == 2:
        return

    element = _menu_boxes[_active_menu]
    menu_box.remove_elements([element])
    manager.remove_element(element)

    _active_menu = 2
    update_menu()

# list format: [(name, function), ...]
def create(menus: list):
    global menu_box, _menu_functions, _menu_boxes

    _menu_functions = [function for name, function in menus]
    menu_buttons = [thorpy.make_button(name,
                                       func=open_menu,
                                       params={"menu_id": i}) for i, (name, _) in enumerate(menus)]
    _menu_boxes = [None] * len(menus)
    minimize_button = thorpy.make_button("Minimize", func=minimize)
    menu_buttons_group = thorpy.make_group(
        menu_buttons + [minimize_button], mode="h")

    menu_box = thorpy.Box(elements=[menu_buttons_group])
    update_menu()
    menu_box.set_topleft(MAIN_VIEW_POSITION)
    return menu_box
