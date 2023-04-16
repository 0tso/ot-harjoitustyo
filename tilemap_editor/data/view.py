import os
from .map import Map
from ..io import map_loader
from .. import camera

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
    pass