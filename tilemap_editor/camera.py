
MOVEMENT_SPEED = 2.0

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 0
    
    def move(self, direction: tuple[int, int]):
        x, y = direction
        self.x += x * MOVEMENT_SPEED
        self.y += y * MOVEMENT_SPEED
    
    def zoom(self, change):
        self.zoom += change
    
    def get_zoom(self):
        return self.zoom

_current_camera = Camera()

def get_current():
    return _current_camera