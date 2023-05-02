import os
import pygame

# tile_id : pygame.Surface
_tiles = {}
_scaled = {}


def get(tile, size=None) -> pygame.Surface:
    """Load a tile surface.

    Args:
        tile: the id of the tile
        size: a single integer that represents the width and height of the tile

    Returns:
        a pygame.Surface
    """

    if tile not in _tiles:
        _tiles[tile] = pygame.image.load(tile).convert_alpha()

    if size is not None:
        if (tile not in _scaled) or (_scaled[tile].get_rect().width != size):
            _scaled[tile] = pygame.transform.scale(_tiles[tile], (size, size))
        return _scaled[tile]

    return _tiles[(tile, size)]


def get_tile_name(tile) -> str:
    """Get the presentable name of a tile, for e.g. GUI presentation.

    Args:
        tile: the id of the tile

    Returns:
        the name of the tile as a string
    """
    filename_full = os.path.basename(tile)
    filename, file_ext = os.path.splitext(filename_full)
    return filename
