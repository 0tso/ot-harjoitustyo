import os

current_file_path = "None"
current_file_name = "None"


def load_from_path(file_path):
    global current_file_path, current_file_name

    current_file_path = file_path
    current_file_name = os.path.basename(current_file_path)
