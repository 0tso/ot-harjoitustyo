import thorpy
from . import main_menu, file_menu, tile_menu

DEFAULT_MARGIN = 5

thorpy.style.FONT_SIZE = 15
thorpy.style.MARGINS = (DEFAULT_MARGIN, DEFAULT_MARGIN, DEFAULT_MARGIN, DEFAULT_MARGIN)

def init():
    global menu

    box = main_menu.create([("File", file_menu.create), ("Tiles", tile_menu.create)])
    menu = thorpy.Menu(elements=[box])

def process_event(event):
    menu.react(event)

def blit():
    for element in menu.get_population():
        element.blit()