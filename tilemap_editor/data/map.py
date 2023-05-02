class Map:
    def __init__(self, tiles={}):
        self.tiles = tiles

    def get_tiles(self, x, y, width, height):
        return [self.get_tile((x+X, y+Y)) for Y in range(height) for X in range(width)]

    def get_tile(self, pos):
        return self.tiles.get(pos, None)

    def set_tile(self, pos, tile_id):
        if tile_id is None:
            if pos in self.tiles:
                del self.tiles[pos]
        else:
            self.tiles[pos] = tile_id
