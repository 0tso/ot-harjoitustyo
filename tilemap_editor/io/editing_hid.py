import pygame
from .. import camera
from ..data import view
from ..gui import manager

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

def inside_gui(pos: tuple[float]) -> bool:
    gui_rects = manager.get_ui_rects()
    for rect in gui_rects:
        if rect.collidepoint(*pos):
            return True
    return False

# HID = Human Interface Device
class EditingHID:
    def __init__(self):
        pass
    
    def process_input(self):
        keys = pygame.key.get_pressed()
        for key, movement in MOVEMENT_MAPPING.items():
            if keys[key]:
                camera.get_current().move(movement)

        if keys[pygame.K_PAGEDOWN]:
            camera.get_current().change_zoom(1)
        if keys[pygame.K_PAGEUP]:
            camera.get_current().change_zoom(-1)
    
    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            if not inside_gui(event.pos):
                view.mouse_event(event.pos, [bool(x) for x in event.buttons])

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not inside_gui(event.pos):
                view.mouse_event(event.pos, pygame.mouse.get_pressed())