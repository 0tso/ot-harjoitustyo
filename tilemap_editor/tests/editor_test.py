import unittest
from ..data import editor
from ..data import view
from ..data.map import Map

class TestEditor(unittest.TestCase):
    def setUp(self) -> None:
        self.tile_0_pixcoord = (0, 0)
        self.tile_1_pixcoord = (view.DEFAULT_TILE_SIZE * 1.5, 0)
        self.tile_2_pixcoord = (view.DEFAULT_TILE_SIZE * 1.5,
                                view.DEFAULT_TILE_SIZE * 1.5)
        view._current_map = Map()
        editor.set_current_selected_tile(None)

    def test_set_current_tile(self):
        editor.set_current_selected_tile(5)
        self.assertEqual(editor._current_tile, 5)
    
    def test_mouse_event(self):
        editor.mouse_event(self.tile_0_pixcoord, (False, False, False))
        self.assertEqual(view.get_tile((0, 0)), None)

        editor.set_current_selected_tile(1)
        editor.mouse_event(self.tile_0_pixcoord, (False, True, True))
        self.assertEqual(view.get_tile((0, 0)), None)

        editor.mouse_event(self.tile_0_pixcoord, (True, False, False))
        self.assertEqual(view.get_tile((0, 0)), 1)

        editor.mouse_event(self.tile_1_pixcoord, (True, False, False))
        self.assertEqual(view.get_tile((1, 0)), 1)

        editor.set_current_selected_tile(2)
        editor.mouse_event(self.tile_2_pixcoord, (True, False, False))
        self.assertEqual(view.get_tile((1, 1)), 2)
        self.assertEqual(view.get_tile((1, 0)), 1)
        self.assertEqual(view.get_tile((2, 2)), None)
    
    def test_undo_redo(self):
        editor.set_current_selected_tile(10)
        editor.mouse_event(self.tile_0_pixcoord, (True, False, False))
        editor.mouse_event(self.tile_1_pixcoord, (True, False, False))
        editor.mouse_event(self.tile_2_pixcoord, (True, False, False))
        self.assertEqual(view.get_tile((0, 0)), 10)
        self.assertEqual(view.get_tile((1, 0)), 10)
        self.assertEqual(view.get_tile((1, 1)), 10)
        editor.mouse_event((0, 0), (False, False, False))

        editor.undo()
        self.assertEqual(view.get_tile((0, 0)), None)
        self.assertEqual(view.get_tile((1, 0)), None)
        self.assertEqual(view.get_tile((1, 1)), None)

        editor.undo()
        self.assertEqual(view.get_tile((0, 0)), None)
        self.assertEqual(view.get_tile((1, 0)), None)
        self.assertEqual(view.get_tile((1, 1)), None)

        editor.redo()
        self.assertEqual(view.get_tile((0, 0)), 10)
        self.assertEqual(view.get_tile((1, 0)), 10)
        self.assertEqual(view.get_tile((1, 1)), 10)

        editor.redo()
        self.assertEqual(view.get_tile((0, 0)), 10)
        self.assertEqual(view.get_tile((1, 0)), 10)
        self.assertEqual(view.get_tile((1, 1)), 10)

        editor.undo()
        editor.set_current_selected_tile(5)
        editor.mouse_event(self.tile_2_pixcoord, (True, False, False))
        editor.redo()
        self.assertEqual(view.get_tile((0, 0)), None)
        self.assertEqual(view.get_tile((1, 1)), 5)
        editor.mouse_event(self.tile_2_pixcoord, (False, False, False))
        editor.undo()
        self.assertEqual(view.get_tile((1, 1)), None)