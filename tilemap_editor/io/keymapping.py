
class KeyMapping:
    def __init__(self, keys: list, func, func_params={}, trigger_once=True):
        self.keys = keys
        self.func = func
        self.func_params = func_params
        self.trigger_once = trigger_once
        self.pressed = False
    
    def update(self, pressed_keys):
        if all(pressed_keys[k] for k in self.keys):
            if (not self.trigger_once) or (not self.pressed):
                self.func(**self.func_params)
                self.pressed = True
        else:
            self.pressed = False