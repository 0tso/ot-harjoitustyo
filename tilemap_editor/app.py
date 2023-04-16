import time
import pygame
from . import window, gui
import tilemap_editor.gui.manager
from .io.editing_hid import EditingHID

TICK_RATE = 144

pygame.init()
window.init()
gui.manager.init()
hid = EditingHID()

clock = pygame.time.Clock()
running = True
previous_time = time.time()
while running:

    # delta time
    clock.tick(TICK_RATE)

    dt = time.time() - previous_time
    previous_time = time.time()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        gui.manager.process_event(event)
        hid.process_event(event)

    # drawing
    window.clear()
    gui.manager.blit()
    window.blit()

pygame.quit()
