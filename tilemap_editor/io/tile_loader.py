import pygame
import os

# tile_id : pygame.Surface
_tiles = {}
_scaled = {}

# size as a single integer: the width and height of the tile in pixels
def get(tile, size=None) -> pygame.Surface:

    if tile not in _tiles:
        _tiles[tile] = pygame.image.load(tile).convert_alpha()
    
    if size is not None:
        if (tile not in _scaled) or (_scaled[tile].get_rect().width != size):
            _scaled[tile] = pygame.transform.scale(_tiles[tile], (size, size))
        return _scaled[tile]

    return _tiles[(tile, size)]


def get_tile_name(tile) -> str:
    filename_full = os.path.basename(tile)
    filename, file_ext = os.path.splitext(filename_full)
    return filename
