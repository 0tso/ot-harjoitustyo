import os
import math
from .map import Map
from ..io import map_loader
from ..gui import file_browser
from .. import camera
from .. import window
from . import tile

DEFAULT_TILE_SIZE = 50

_current_map = Map()
_current_map_path = ""
camera.set_current(camera.Camera(
    movement_speed=5, zoom_speed=0.01, max_zoom=-4, zoom_scale=2))


def load_map(file_path: str):
    global _current_map, _current_map_path

    _current_map_path = file_path

    tiles = map_loader.load_from_path(file_path)
    _current_map = Map(tiles)


def save_map_to_path(file_path: str):
    global _current_map_path
    map_loader.save_to_path(_current_map.tiles, file_path)
    _current_map_path = file_path


def save_map():
    if _current_map_path != "":
        save_map_to_path(_current_map_path)
    else:
        file_path = file_browser.open(save=True)
        if file_path:
            save_map_to_path(file_path)


def get_current_map_name():
    name = os.path.basename(_current_map_path)
    return name


def blit():
    """Draw the current view onto the screen."""
    cam = camera.get_current()
    tile_size = DEFAULT_TILE_SIZE * cam.get_zoom_factor()
    vertical_tile_amount = math.ceil(window.WINDOW_HEIGHT / tile_size) + 1
    horizontal_tile_amount = math.ceil(window.WINDOW_WIDTH / tile_size) + 1
    min_x = math.floor(cam.x / tile_size)
    min_y = math.floor(cam.y / tile_size)
    tiles = _current_map.get_tiles(
        min_x, min_y, horizontal_tile_amount, vertical_tile_amount)
    for i, tile_id in enumerate(tiles):
        if tile_id is not None:
            x_i = min_x + i % horizontal_tile_amount
            y_i = min_y + i // horizontal_tile_amount
            x = x_i * tile_size - cam.x
            y = y_i * tile_size - cam.y
            tile.blit_at(tile_id, (x, y), tile_size)


def tile_coords_from_screen_pos(pos: tuple[int]) -> tuple[int]:
    """Get tile X & Y from screen pixel coordinates.

    Args:
        pos: a tuple of integers denoting the screen position in pixels

    Returns:
        a tuple of ints denoting the tile X/Y position.
    """
    pos_x, pos_y = pos
    cam = camera.get_current()
    tile_size = DEFAULT_TILE_SIZE * cam.get_zoom_factor()
    min_x = math.floor(cam.x / tile_size)
    min_y = math.floor(cam.y / tile_size)

    dist_x = pos_x + (cam.x % tile_size)
    dist_y = pos_y + (cam.y % tile_size)

    return (min_x + dist_x // tile_size, min_y + dist_y // tile_size)


def get_tile(pos: tuple[int, int]):
    """Get tile_id at a tile position.

    Args:
        pos: the tile position as tuple of ints.

    Returns:
        the tile_id of the tile in question
    """
    return _current_map.get_tile(pos)


def set_tile(pos: tuple[int, int], tile_id):
    _current_map.set_tile(pos, tile_id)
