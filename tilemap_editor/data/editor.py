from . import view

_current_tile = None
_changes = []
_current_change_batch = []
_undo_amount = 0


def set_current_selected_tile(tile_id):
    global _current_tile

    _current_tile = tile_id


def mouse_event(pos, buttons: list[bool]):
    """Process a mouse event.

    Args:
        pos: the position of the mouse in pixels, top left being (0, 0).
        buttons: the statuses of the 3 mouse buttons (left, middle, right) as booleans, denoting whether they are pressed.
    """
    global _undo_amount

    left, mid, right = buttons

    if left:
        tile_pos = view.tile_coords_from_screen_pos(pos)
        old = view.get_tile(tile_pos)
        if (_current_tile is not None) and (_current_tile != old):
            new = _current_tile
            view.set_tile(tile_pos, new)

            if _undo_amount > 0:
                del _changes[-_undo_amount:]
                _undo_amount = 0
            _current_change_batch.append((tile_pos, new, old))
    elif len(_current_change_batch) > 0:
        _changes.append(tuple(_current_change_batch))
        _current_change_batch.clear()


def undo():
    global _undo_amount

    if len(_changes) > _undo_amount:
        _undo_amount += 1
        for (pos, new, old) in _changes[-_undo_amount]:
            view.set_tile(pos, old)


def redo():
    global _undo_amount
    if _undo_amount > 0:
        for (pos, new, old) in _changes[-_undo_amount]:
            view.set_tile(pos, new)
        _undo_amount -= 1
