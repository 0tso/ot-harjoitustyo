import os
import math
from .map import Map
from ..io import map_loader
from .. import camera
from .. import window
from . import tile

TILE_SIZE = 50
ZOOM_SIZE_MULTIPLIER = 1.25

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
    vertical_tile_amount = math.ceil(window.WINDOW_HEIGHT / TILE_SIZE) + 1
    horizontal_tile_amount = math.ceil(window.WINDOW_WIDTH / TILE_SIZE) + 1
    min_x = math.floor(cam.x / TILE_SIZE)
    min_y = math.floor(cam.y / TILE_SIZE)
    tiles = _current_map.get_tiles(min_x, min_y, vertical_tile_amount, horizontal_tile_amount)
    for i, tile_id in enumerate(tiles):
        if tile_id != None:
            x_i = i % vertical_tile_amount
            y_i = i // vertical_tile_amount
            x = x_i * TILE_SIZE - cam.x
            y = y_i * TILE_SIZE - cam.y
            tile.blit_at(tile_id, (x, y), TILE_SIZE)