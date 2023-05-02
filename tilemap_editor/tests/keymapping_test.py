import unittest
from ..io.keymapping import KeyMapping


class TestKeyMapping(unittest.TestCase):
    def setUp(self):
        self.a = 0

    def set_a(self):
        self.a += 1

    def set_a_params(self, value):
        self.a += value

    def test_press(self):
        m = KeyMapping([1, 2, 3], self.set_a, trigger_once=True)
        keys = {2: True, 1: True, 3: True, 4: True}
        m.update(keys)
        self.assertEqual(self.a, 1)
        m.update(keys)
        self.assertEqual(self.a, 1)
        m.update({1: True, 2: True, 3: False, 4: True})
        self.assertEqual(self.a, 1)
        m.update(keys)
        self.assertEqual(self.a, 2)

    def test_params(self):
        m = KeyMapping([1, 5], self.set_a_params, func_params={"value": 5})
        keys = {1: True, 5: True, 6: False, 4: True}
        m.update(keys)
        self.assertEqual(self.a, 5)
