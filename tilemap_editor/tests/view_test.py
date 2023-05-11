import os
import unittest
from ..data import view
from ..data.map import Map


class TestView(unittest.TestCase):
    def setUp(self) -> None:
        view._current_map = Map()
        self.dirname = os.path.dirname(__file__)
        self.test_map_path = os.path.join(
            os.path.dirname(__file__), "test.map")
        self.tile_A = os.path.join(self.dirname, "A")
        self.tile_B = os.path.join(self.dirname, "B")

    def test_set_current_map(self):
        view.load_map(self.test_map_path)
        self.assertEqual(view.get_current_map_name(), "test.map")

        self.assertEqual(view.get_tile((0, 0)), self.tile_A)
        self.assertEqual(view.get_tile((0, 1)), self.tile_A)
        self.assertEqual(view.get_tile((1, 1)), self.tile_B)
        self.assertEqual(view.get_tile((1, 2)), None)
