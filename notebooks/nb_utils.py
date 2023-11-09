"""
Utilities for ipython notebooks
"""

import os
import sys


def set_path():
    """
    Allows notebooks to import modules from the rest of the project, outside of the 
    notebooks folder.
    For example, in a notebook cell, run:
    ```
        from nb_utils import set_path
        set_path()
    ```
    This will add '/path/to/project/root/' to the python path.
    Then is it is possible to import from the main package into the notebook, e.g.
    ```
        from timtam.config import DATA_DIR
    ```
    """
    # Assuming this module is in `<repo_root>/<notebook_folder>`
    # NB if this module is moved or the above folder structure changes, this will break.
    this_module = os.path.dirname(__file__)
    project_root = os.path.dirname(this_module)
    src_path = os.path.join(project_root)

    for path in [src_path]:
        if path not in sys.path:
            sys.path.append(path)


if __name__ == "__main__":
    set_path()
    for p in sys.path:
        print(p)
