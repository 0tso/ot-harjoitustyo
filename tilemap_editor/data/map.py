
# TESTING
import os
TEST_GRASS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets", "grass.png")
TEST_MAP = {(0,0): TEST_GRASS, (1, 1): TEST_GRASS, (1, 2): TEST_GRASS, (5,5): TEST_GRASS, (0, 1): TEST_GRASS}

class Map:
    def __init__(self, tiles):
        # TESTING
        self.tiles = TEST_MAP
    
    def get_tiles(self, x, y, width, height):
        return [self.get_tile(x+X, y+Y) for Y in range(height) for X in range(width)]

    def get_tile(self, x, y):
        return self.tiles.get((x, y), None)

    def set_tile(self, x, y, tile_id):
        self.tiles[(x, y)] = tile_id
    