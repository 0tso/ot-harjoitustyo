import os

IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".raw"]

current_dir_path = ""
current_dir_tiles = []


def load(directory_path=None):
    global current_dir_path

    if directory_path and directory_path != current_dir_path:
        current_dir_tiles.clear()
        current_dir_path = directory_path

        for item in os.listdir(directory_path):
            filename, file_extension = os.path.splitext(item)
            file_path = os.path.join(directory_path, filename + file_extension)
            if os.path.isfile(file_path):
                if file_extension in IMAGE_FORMATS:
                    current_dir_tiles.append(file_path)

    return current_dir_tiles
