import unittest
from ..data.map import Map

class TestMap(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_empty(self):
        map = Map()

        self.assertEqual(map.get_tile(0, 0), None)
        self.assertTrue(all(x is None for x in map.get_tiles(-15, 61, 24, 612)))

        map.set_tile(0, 0, tile_id=6)
        self.assertEqual(map.get_tile(0, 0), 6)
        map.set_tile(2, 7, tile_id=6)
        tiles = map.get_tiles(0, 0, 10, 10)
        self.assertEqual(tiles.count(6), 2)
    
    def test_prefilled(self):
        map = Map({(0,0): 1, (1,1): 1, (2,2): 1})

        self.assertEqual(map.get_tile(0, 1), None)
        self.assertEqual(map.get_tile(1, 1), 1)
        self.assertEqual(map.get_tiles(0, 0, 2, 2).count(1), 2)