class Map:
    def __init__(self, tiles):
        self.tiles = tiles
    
    def get_tiles(self, x, y, width, height):
        return [self.get_tile(x+X, y+Y) for Y in range(height) for X in range(width)]

    def get_tile(self, x, y):
        return self.tiles.get((x, y), None)

    def set_tile(self, x, y, tile_id):
        self.tiles[(x, y)] = tile_id
    