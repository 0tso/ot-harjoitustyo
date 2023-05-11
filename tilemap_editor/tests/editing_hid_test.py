import pygame
import unittest
from ..io.editing_hid import EditingHID
from ..io.keymapping import KeyMapping
from ..gui import manager
from .. import window

pygame.init()
window.init()
manager.init()


class TestEditingHID(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 0
        self.mouse_pos = (0, 0)
        self.mouse_buttons = (False, False, False)

    def test(self, a=None):
        if a is not None:
            self.a = a

    def mouse_func(self, pos, buttons: tuple[bool, bool, bool]):
        self.mouse_pos = pos
        self.mouse_buttons = tuple(buttons)

    def test_basic(self):
        keymappings = [
            KeyMapping([pygame.K_0], func=self.test)
        ]
        hid = EditingHID(keymappings, self.mouse_func)
        hid.process_input()
        self.assertFalse(keymappings[0].pressed)

        mouse_event = pygame.event.Event(pygame.MOUSEMOTION, pos=(
            500, 500), buttons=(False, False, True))
        hid.process_event(mouse_event)
        self.assertEqual(self.mouse_buttons, (False, False, True))
        self.assertEqual(self.mouse_pos, (500, 500))
