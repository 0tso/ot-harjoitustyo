# 2D tilemap editor

An editor for 2D tile-based maps.

## Documentation

* [Usage instructions](./documentation/usage_instructions.md)
* [Architecture](./documentation/architecture.md)
* [Requirements specification](./documentation/requirements_specification.md)
* [Changelog](./documentation/changelog.md)
* [Testing](./documentation/testing.md)
* [Working time records](./documentation/working_time_records.md)

## Installation

1. Clone the repository:
```bash
git clone git@github.com:0tso/tilemap-editor.git
cd tilemap-editor
```
2. Install the necessary dependencies using `poetry`:
```bash
poetry install
```

## Startup & commands

You can start the program using:
```bash
poetry run invoke start
```

or run the tests:
```bash
poetry run invoke test
```

or generate a coverage report:
```bash
poetry run invoke coverage-report
```

For more in-depth usage information, see the [usage instructions](./documentation/usage_instructions.md).