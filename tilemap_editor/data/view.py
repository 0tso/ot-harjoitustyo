import os
import math
from .map import Map
from ..io import map_loader
from .. import camera
from .. import window
from . import tile

DEFAULT_TILE_SIZE = 50
ZOOM_SIZE_MULTIPLIER = 10

_current_map = Map([])
_current_map_path = ""

def load_map(file_path: str):
    global _current_map, _current_map_path

    _current_map_path = file_path

    tiles = map_loader.load_from_path(file_path)
    _current_map = Map(tiles)


def get_current_map_name():
    name = os.path.basename(_current_map_path)
    return name


def blit():
    cam = camera.get_current()
    tile_size = DEFAULT_TILE_SIZE + cam.zoom * ZOOM_SIZE_MULTIPLIER
    vertical_tile_amount = math.ceil(window.WINDOW_HEIGHT / tile_size) + 1
    horizontal_tile_amount = math.ceil(window.WINDOW_WIDTH / tile_size) + 1
    min_x = math.floor(cam.x / tile_size)
    min_y = math.floor(cam.y / tile_size)
    tiles = _current_map.get_tiles(min_x, min_y, horizontal_tile_amount, vertical_tile_amount)
    for i, tile_id in enumerate(tiles):
        if tile_id != None:
            x_i = min_x + i % horizontal_tile_amount
            y_i = min_y + i // horizontal_tile_amount
            x = x_i * tile_size - cam.x
            y = y_i * tile_size - cam.y
            tile.blit_at(tile_id, (x, y), tile_size)