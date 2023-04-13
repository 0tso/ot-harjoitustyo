import pygame
import time
from . import window, gui
from .gui import manager

TICK_RATE = 144

pygame.init()
window.init()
gui.manager.init()

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
    
    # drawing
    window.clear()
    
    gui.manager.blit()

    window.blit()


pygame.quit()