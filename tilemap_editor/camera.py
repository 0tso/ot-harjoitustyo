import math


class Camera:
    def __init__(self, movement_speed, zoom_speed, max_zoom, zoom_scale):
        self.x = 0
        self.y = 0
        self.zoom = 0
        self.movement_speed = movement_speed
        self.zoom_speed = zoom_speed
        self.max_zoom = max_zoom
        self.zoom_scale = zoom_scale

    def move(self, direction: tuple[int, int]):
        x, y = direction
        self.x += x * self.movement_speed
        self.y += y * self.movement_speed

    def change_zoom(self, change):
        self.zoom = max(self.max_zoom, self.zoom + change * self.zoom_speed)

    def get_zoom_factor(self):
        """Returns the number a tile's dimensions have to be multiplied by in order to account for the zoom."""
        return math.pow(self.zoom_scale, self.zoom)


_current_camera = None


def set_current(cam: Camera):
    global _current_camera

    _current_camera = cam


def get_current() -> Camera:
    return _current_camera
