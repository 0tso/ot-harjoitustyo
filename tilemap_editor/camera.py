class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 0
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def zoom(self, change):
        self.zoom += change
    
    def get_zoom(self):
        return self.zoom

_current_camera = Camera()

def get_current():
    return _current_camera