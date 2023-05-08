# Description of the architecture

## File & package structure

```mermaid
flowchart LR
    tilemap_editor <---> data
    tilemap_editor <---> io
    tilemap_editor <---> gui

    data ---> io
    gui ---> data
```

* The top-level `tilemap_editor` package contains modules that manage the whole program, such as `app.py`, and modules that are extensively used in inter-package communication, such as `camera.py`.
* The `data` package contains modules that deal with rendering, storing and modifying the tilemaps: the central pieces of the whole program, so to say.
* The `io` ("Input/Output") package contains modules that deal with either interacting with the file system or with the human input coming into the system via, for example, keyboard and mouse.
* The `gui` ("Graphical User Interface") package contains modules that handle the rest of the user interaction outside moving around and editing the tilemap.

## Module & class interaction

```mermaid
classDiagram
    EditingHID ..> Camera
    EditingHID ..> editor
    editor ..> view
    note for view "the view module might manage and \n combine multiple maps in the future"
    view -- "1" Camera
    view -- "1" Map
```
_Above a simplified representation of the core module interaction._

- The `EditingHID` (singleton) class manages the commands related to moving around and editing the map via the user's keyboard & mouse and relies this information forward (mainly to the `Camera` (singleton) class and the `editor` module).
- The `editor` module manages and stores the individual changes (and undos + redos) made by the user to the tilemap and relies those to the `view` module.
- The `view` module manages and saves the `Map`(s) that the user sees: the user's "view", so to speak. Drawing is done based on the information (position in the world) from the `Camera` singleton.


## Example sequence diagram of module interaction

The following sequence diagram showcases the module interaction whenever the user presses the button for loading a map file.

```mermaid
sequenceDiagram
    main ->> file_menu: open_file_browser()
    file_menu ->> file_browser: open()
    file_browser -->> file_menu: file_path
    file_menu ->> view: load_map(file_path)
    view ->> map_loader: load_from_path(file_path)
    map_loader -->> view: tiles
    Note over view: saves tiles into _current_map
```

And the following sequence diagram shows what happens whenever the user clicks on a position on the screen:

```mermaid
sequenceDiagram
    app ->> EditingHID: process_event(event)
    EditingHID ->> gui.manager: get_ui_rects()
    gui.manager -->> EditingHID: gui_rects
    Note over EditingHID: checks whether or not the point is within the GUI
    Note over EditingHID: if not, continue
    EditingHID ->> editor: mouse_event(pos, buttons)
    editor ->> view: tile_coords_from_screen_pos()
    view -->> editor: tile_pos
    editor ->> view: get_tile(tile_pos)
    view ->> Map: get_tile(tile_pos)
    Map -->> view: tile
    view -->> editor: old
    Note over editor: the old tile is saved for undo and redo
    editor ->> view: set_tile(tile_pos, new)
    view ->> Map: set_tile(tile_pos, new)
```