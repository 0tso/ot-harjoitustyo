import thorpy
import thorpy.miscgui.functions
from . import main_menu, file_menu, tile_menu

DEFAULT_MARGIN = 5

thorpy.style.FONT_SIZE = 15
thorpy.style.MARGINS = (DEFAULT_MARGIN, DEFAULT_MARGIN, DEFAULT_MARGIN, DEFAULT_MARGIN)

def init():
    global menu

    box = main_menu.create([("File", file_menu.create), ("Tiles", tile_menu.create)])
    menu = thorpy.Menu(elements=[box])
    thorpy.miscgui.functions.set_current_menu(menu)

def process_event(event):
    menu.react(event)

def blit():
    for e in menu.get_population():
        e.blit()

def add_element(element):
    menu.add_to_population(element)

def remove_element(element):
    menu.remove_from_population(element)