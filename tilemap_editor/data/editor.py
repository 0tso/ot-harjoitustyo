from . import view

_current_tile = None
_changes = []
_undo_amount = 0

def set_current_selected_tile(tile_id):
    global _current_tile

    _current_tile = tile_id

def mouse_event(pos, buttons: list[bool]):
    global _undo_amount

    left, mid, right = buttons
    tile_pos = view.tile_coords_from_screen_pos(pos)
    old = view.get_tile(tile_pos)
    if (_current_tile is not None) and left and (_current_tile != old):
        new = _current_tile
        view.set_tile(tile_pos, new)

        if _undo_amount > 0:
            del _changes[-_undo_amount:]
            _undo_amount = 0
        _changes.append((tile_pos, new, old))

def undo():
    global _undo_amount

    if len(_changes) > _undo_amount:
        _undo_amount += 1
        pos, new, old = _changes[-_undo_amount]
        view.set_tile(pos, old)

def redo():
    global _undo_amount

    if _undo_amount > 0:
        pos, new, old = _changes[-_undo_amount]
        _undo_amount -= 1
        view.set_tile(pos, old)