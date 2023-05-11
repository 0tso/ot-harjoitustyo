import thorpy
from ..io import tileset_loader, tile_loader
from ..data import editor
from . import file_browser, main_menu

TILES_PER_ROW = 3
TILE_MARGIN = 5


def set_selected_tile(tile_id):
    editor.set_current_selected_tile(tile_id)


def add_tiles(tiles):
    global _tiles_box, _menu_width

    tile_size = (_menu_width -
                 (TILES_PER_ROW + 1) * TILE_MARGIN) / TILES_PER_ROW
    current_row = []

    def add_row():
        group = thorpy.make_group(current_row)
        _tiles_box.append_element(group)

    for tile in tiles:
        img = tile_loader.get(tile, tile_size)
        btn = thorpy.make_image_button(img_normal=img)
        btn.user_func = set_selected_tile
        btn.user_params = {"tile_id": tile}
        current_row.append(btn)

        if len(current_row) == TILES_PER_ROW:
            add_row()
            current_row.clear()

    # fill the last row with empty thorpy.Elements if it has more than one (but less than TILES_PER_ROW) tiles
    if len(current_row) > 0:
        for _ in range(TILES_PER_ROW - len(current_row)):
            e = thorpy.Element()
            e.set_size((tile_size, tile_size))
            current_row.append(e)
        add_row()

    thorpy.store(_tiles_box)
    _tiles_box.fit_children()
    _tiles_box.set_size((_menu_width, None))


def open_file_browser():
    dir_path = file_browser.open(directory=True)
    if dir_path:
        dir_text.set_text("Directory:\n" + ".." +
                          tileset_loader.current_dir_path[-20:])
        dir_text.scale_to_title()
        tiles = tileset_loader.load(dir_path)
        add_tiles(tiles)
        main_menu.reload()


def create(width):
    global dir_text, _tiles_box, _menu_width

    _menu_width = width
    dir_text = thorpy.make_text(
        "Directory:\n" + ".." + tileset_loader.current_dir_path[-20:])
    browse_dirs_button = thorpy.make_button(
        "Browse directories", func=open_file_browser)

    _tiles_box = thorpy.Box(elements=[dir_text, browse_dirs_button])
    add_tiles(tileset_loader.load())
    return _tiles_box
