import pygame
from ..io import tile_loader


class Tile(pygame.sprite.Sprite):

    def __init__(self, tile_id):
        super().__init__()
        self.tile_id = tile_id
    

    def blit_at(self, pos, size):
        img = tile_loader.get(self.tile_id, size)
        img.get_rect().topleft = pos
        img.blit()
