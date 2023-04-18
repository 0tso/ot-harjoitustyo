```mermaid
classDiagram
    note for view "the view module might manage and \n combine multiple maps in the future"
    view -- "1" Camera
    EditingHID ..> Camera
    EditingHID ..> view
    view -- "1" Map
```