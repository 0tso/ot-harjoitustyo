
class KeyMapping:
    def __init__(self, keys: list, func, func_params=None, trigger_once=True, block=None):
        """Initialize the mapping.

        Args:
            keys: the list of pygame.keys that are required for the keymapping to be activated.
            func: the function to be called when the keymapping is activated
            func_params: the parameters to be passed to func as a dictionary (**kwargs)
            trigger_once: whether or not to wait for key release on activation for the next activation.
            block: a list of pygame.keys that block the activation
        """
        self.keys = keys
        self.func = func
        self.func_params = {} if func_params is None else func_params
        self.trigger_once = trigger_once
        self.block = [] if block is None else block
        self.pressed = False

    def update(self, pressed_keys):
        if all(pressed_keys[k] for k in self.keys):
            if ((not self.trigger_once) or (not self.pressed)) and not any(pressed_keys[k] for k in self.block):
                self.func(**self.func_params)
                self.pressed = True
        else:
            self.pressed = False
