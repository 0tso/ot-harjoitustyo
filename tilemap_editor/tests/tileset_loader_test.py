import unittest
import os
from ..io import tileset_loader

class TestTilesetLoader(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.dirname(os.path.realpath(__file__))
        
    def test_empty_folder(self):
        path = os.path.join(self.dirname, "empty")
        tileset_loader.load(path)
        self.assertEqual(tileset_loader.current_dir_path, path)
        self.assertEqual(len(tileset_loader.load()), 0)
    
    def test_folder_with_4_tiles(self):
        path = os.path.join(self.dirname, "4_tiles")
        tileset_loader.load(path)
        self.assertEqual(tileset_loader.current_dir_path, path)
        self.assertEqual(len(tileset_loader.load()), 4)