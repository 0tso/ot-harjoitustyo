import pygame
from .. import camera
from ..data import view, editor
from ..gui import manager
from .keymapping import KeyMapping

MOVEMENT_MAPPING = {
    # WASD
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),

    # arrow keys
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

KEYMAPPINGS = [
    KeyMapping([pygame.K_PAGEDOWN], camera.get_current().change_zoom,
               func_params={"change": 1}, trigger_once=False),
    KeyMapping([pygame.K_PAGEUP], camera.get_current().change_zoom,
               func_params={"change": -1}, trigger_once=False),
    KeyMapping([pygame.K_LCTRL, pygame.K_s], view.save_map),
    KeyMapping([pygame.K_LCTRL, pygame.K_z], editor.undo),
    KeyMapping([pygame.K_LCTRL, pygame.K_y], editor.redo),
]


def is_inside_gui(pos: tuple[float]) -> bool:
    """Determines whether or not a pixel position is within the GUI.

    Args:
        pos: the position as a tuple of integers, denoting pixel coordinates

    Returns:
        a boolean—whether or not the pixel is within GUI confines.
    """
    gui_rects = manager.get_ui_rects()
    for rect in gui_rects:
        if rect.collidepoint(*pos):
            return True
    return False


class EditingHID:
    """A Human Interface Device (HID) class, meant for input processing from HID devices such as a keyboard and a mouse."""

    def __init__(self):
        pass

    def process_input(self):
        keys = pygame.key.get_pressed()
        for key, movement in MOVEMENT_MAPPING.items():
            if not keys[pygame.K_LCTRL] and keys[key]:
                camera.get_current().move(movement)

        for mapping in KEYMAPPINGS:
            mapping.update(keys)

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            if not is_inside_gui(event.pos):
                editor.mouse_event(event.pos, [bool(x) for x in event.buttons])

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_inside_gui(event.pos):
                editor.mouse_event(event.pos, pygame.mouse.get_pressed())
