# Overview of testing

## Unit testing

Most of the modules and classes outside the field of GUI have separate unit tests written for them.

Some tests, such as tests for modules that load / save data from / to files, save temporary files to the `tests` folder. An example of this is the `map_loader_test.py`, which creates and subsequently deletes the file `temp.map` during testing.

Similarly, some tests (at the moment only `editing_hid_test.py`) may require the pygame engine to be up and running, resulting in a brief flash of the pygame window during testing.

Barring the GUI modules, which are excluded from the testing, the branch coverage of the tests is 80%.

## System testing

System testing has been done manually.

The application has been confirmed to work on Ubuntu 22.04.

All points listed in the [requirements specification](./requirements_specification.md) have been manually confirmed to work.