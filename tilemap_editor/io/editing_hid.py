import pygame
from .. import camera

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

# HID = Human Interface Device
class EditingHID:
    def __init__(self):
        pass
    
    def process_input(self):
        keys = pygame.key.get_pressed()
        for key, movement in MOVEMENT_MAPPING.items():
            if keys[key]:
                camera.get_current().move(movement)