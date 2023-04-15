import pygame
import os

# (tile_id=path, pixel_size) : pygame.Surface
tiles = {}

# size as a single integer: the width and height of the tile in pixels
def get(tile, size=None):

    if (tile, size) not in tiles:
        if size == None:
            tiles[(tile, size)] = pygame.image.load(tile).convert_alpha()
        else:
            original = get(tile)
            # assuming that the scale()-function creates a new Surface
            new = pygame.transform.scale(original, (size, size))
            tiles[(tile, size)] = new

    return tiles[(tile, size)]


def get_tile_name(tile):
    filename_full = os.path.basename(tile)
    filename, file_ext = os.path.splitext(filename_full)
    return filename
