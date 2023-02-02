## F() function

The F function can perform operations on values from the database without pulling them into pythons memory. This can
avoid race conditions when incrementing voting values for instance.

## Modules

`__init__.py` makes a directory a Python module. Putting this file in the project root causes problems when running
django tests. This file is not required to make a Python module as of the latest versions of Python.