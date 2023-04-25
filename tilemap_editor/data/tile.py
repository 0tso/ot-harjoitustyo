from ..io import tile_loader
from .. import window


def blit_at(tile_id, pos, size):
    img = tile_loader.get(tile_id, size)
    window.blit(img, pos)
