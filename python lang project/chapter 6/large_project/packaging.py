"""
my_package
|----__init__.py
|---- my_package.py
    |---- my_subpackage
        |---- __init__.py
        |---- my_subpackage.py

# using __init.__.py to import all you modules
    -inside the parent __init__.py file import the modules
    -them from you code files, when you need to import write:
        from my_package import File

# to access everything in you package from a subfolder
    -inside the parent __init__.py file write:
        __all__ = ['my_subpackage']
    - now from inside my_subpackage folder's python file:
        my _ package import * # will import everythin inside my_package
        
"""