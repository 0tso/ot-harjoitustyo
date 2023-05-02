import os

IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".raw"]
DEFAULT_DIR = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "..", "..", "assets")

current_dir_path = ""
current_dir_tiles = []


def load(directory_path=None):
    """Load a tileset either from a specific directory or the current directory.

    Args:
        directory_path: the path of the directory from which to load the tiles. If left undefined, loads the current directory.

    Returns:
        a list of tile_ids
    """
    global current_dir_path

    if directory_path and directory_path != current_dir_path:
        current_dir_tiles.clear()
        current_dir_path = directory_path

        for item in os.listdir(directory_path):
            filename, file_extension = os.path.splitext(item)
            file_path = os.path.join(directory_path, filename + file_extension)
            if os.path.isfile(file_path) and file_extension in IMAGE_FORMATS:
                current_dir_tiles.append(file_path)

    return current_dir_tiles


load(DEFAULT_DIR)
