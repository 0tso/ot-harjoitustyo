import pygame
from .. import camera
from ..data import view, editor
from ..gui import manager
from .keymapping import KeyMapping

KEYMAPPINGS = [
    # Movement

    # WASD
    KeyMapping([pygame.K_w], camera.get_current().move, func_params={"direction": (0, -1)}, trigger_once=False, block=[pygame.K_LCTRL]),
    KeyMapping([pygame.K_s], camera.get_current().move, func_params={"direction": (0, 1)}, trigger_once=False, block=[pygame.K_LCTRL]),
    KeyMapping([pygame.K_a], camera.get_current().move, func_params={"direction": (-1, 0)}, trigger_once=False, block=[pygame.K_LCTRL]),
    KeyMapping([pygame.K_d], camera.get_current().move, func_params={"direction": (1, 0)}, trigger_once=False, block=[pygame.K_LCTRL]),

    # arrow keys
    KeyMapping([pygame.K_UP], camera.get_current().move, func_params={"direction": (0, -1)}, trigger_once=False, block=[pygame.K_LCTRL]),
    KeyMapping([pygame.K_DOWN], camera.get_current().move, func_params={"direction": (0, 1)}, trigger_once=False, block=[pygame.K_LCTRL]),
    KeyMapping([pygame.K_LEFT], camera.get_current().move, func_params={"direction": (-1, 0)}, trigger_once=False, block=[pygame.K_LCTRL]),
    KeyMapping([pygame.K_RIGHT], camera.get_current().move, func_params={"direction": (1, 0)}, trigger_once=False, block=[pygame.K_LCTRL]),

    # The rest
    KeyMapping([pygame.K_PAGEDOWN], camera.get_current().change_zoom, func_params={"change": 1}, trigger_once=False),
    KeyMapping([pygame.K_PAGEUP], camera.get_current().change_zoom, func_params={"change": -1}, trigger_once=False),
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

    def __init__(self, keymappings, mouse_func):
        self.keymappings = keymappings
        self.mouse_func = mouse_func

    def process_input(self):
        """Processes the keyboard input accumulated during the frame.
        To be called once per frame."""
        keys = pygame.key.get_pressed()
        for mapping in self.keymappings:
            mapping.update(keys)

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            if not is_inside_gui(event.pos):
                self.mouse_func(event.pos, (bool(x) for x in event.buttons))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not is_inside_gui(event.pos):
                self.mouse_func(event.pos, pygame.mouse.get_pressed())
