import pygame

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
    def __init__(self, movementhandler, mousehandler):
        self.movementhandler = movementhandler
        self.mousehandler = mousehandler
    
    def process_input(self):
        keys = pygame.key.get_pressed()
        for key, movement in MOVEMENT_MAPPING.items():
            if keys[key]:
                self.movementhandler.move(movement)

        if keys[pygame.K_PAGEDOWN]:
            self.movementhandler.zoom(1)
        if keys[pygame.K_PAGEUP]:
            self.movementhandler.zoom(-1)
    
    # TODO:
    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            self.mousehandler.mouse_motion(event.pos[0], event.pos[1], [bool(x) for x in event.buttons])
            self.mousehandler.mouse_event(event.pos[0], event.pos[1], [bool(x) for x in event.buttons])

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.movementhandler.mouse_event(event.pos[0], event.pos[1], pygame.mouse.get_pressed())