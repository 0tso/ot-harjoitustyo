import thorpy
from . import main_view

thorpy.style.FONT_SIZE = 15
thorpy.style.MARGINS = (5, 5, 5, 5)

def init():
    global menu

    box = main_view.create()
    menu = thorpy.Menu(elements=[box])

def process_event(event):
    menu.react(event)

def blit():
    for element in menu.get_population():
        element.blit()