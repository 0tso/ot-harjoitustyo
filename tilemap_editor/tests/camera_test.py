import unittest
from .. import camera
from ..camera import Camera

class TestCamera(unittest.TestCase):
    def setUp(self) -> None:
        self.cam = Camera(movement_speed=2, zoom_speed=0.5, min_zoom=-5, zoom_scale=2)

    def test_movement(self):
        self.cam.move((-1, 0))
        self.assertEqual(self.cam.x, -2)
        self.assertEqual(self.cam.y, 0)

        self.cam.move((1, 1))
        self.assertEqual(self.cam.x, 0)
        self.assertEqual(self.cam.y, 2)

    def test_zoom(self):
        self.cam.change_zoom(2)
        self.assertEqual(self.cam.get_zoom_factor(), 2 ** 1)

        self.cam.change_zoom(-12)
        self.assertEqual(self.cam.get_zoom_factor(), 2 ** (-5))

        self.cam.change_zoom(-1)
        self.assertEqual(self.cam.get_zoom_factor(), 2 ** (-5))