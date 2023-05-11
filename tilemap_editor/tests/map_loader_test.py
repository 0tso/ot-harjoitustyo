import os
import unittest
from ..io import map_loader


class TestMapLoader(unittest.TestCase):
    def setUp(self) -> None:
        self.dirname = os.path.dirname(__file__)
        self.temp_map = os.path.join(self.dirname, "temp.map")
        self.test_map = os.path.join(self.dirname, "test.map")

    def test_load_save(self):
        tiles = {(0, 0): os.path.join(self.dirname, "A"), (66, 123): os.path.join(
            self.dirname, "empty", "testtesttest"), (109215, 61235): os.path.join(self.dirname, "..", "no_idea.jpg")}
        map_loader.save_to_path(tiles, self.temp_map)
        ret = map_loader.load_from_path(self.temp_map)
        self.assertEqual(tiles, ret)
        os.remove(self.temp_map)
