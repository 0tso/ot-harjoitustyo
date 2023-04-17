
MOVEMENT_SPEED = 2.0
ZOOM_SPEED = 0.05

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 1
    
    def move(self, direction: tuple[int, int]):
        x, y = direction
        self.x += x * MOVEMENT_SPEED
        self.y += y * MOVEMENT_SPEED
    
    def change_zoom(self, change):
        self.zoom += change * ZOOM_SPEED

_current_camera = Camera()

def get_current():
    return _current_camera