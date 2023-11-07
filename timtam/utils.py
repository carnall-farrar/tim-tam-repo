import os

from timtam.config import (
    STATIC_DIR,
    DATA_DIR,
    RAW_DIR,
    PROCESSED_DIR,
    OUTPUT_DIR,
)


def get_root_path() -> str:
    """Automatically detect the full path leading to the repo folder.
    Assuming directory structure is:
        /this/project/path/repo_name/package/this_module.py
    Return:
        /path/to/this/project/repo_name
    """
    module_path = os.path.abspath(__file__)
    package_path = os.path.dirname(module_path)
    repo_path = os.path.dirname(package_path)
    return repo_path


def get_project_path(*lower_paths):
    """If repo directory is
        `/path/to/repo/project`
    and `lower_paths` is `file.txt`
    then return
        `/path/to/repo/project/file.txt`

    Alternatively, if `lower_paths` is ["subfolder", "file.txt"]
    then return
        `/path/to/repo/project/subfolder/file.txt`
    etc for any number of subfolder layers.
    """
    root = get_root_path()
    path = os.path.join(root, *lower_paths)
    return path


def get_static_path(*lower_paths):
    path = get_project_path(STATIC_DIR, *lower_paths)
    return path


def get_raw_path(*lower_paths):
    path = get_project_path(DATA_DIR, RAW_DIR, *lower_paths)
    return path


def get_processed_path(*lower_paths):
    path = get_project_path(DATA_DIR, PROCESSED_DIR, *lower_paths)
    return path


def get_output_path(*lower_paths):
    path = get_project_path(DATA_DIR, OUTPUT_DIR, *lower_paths)
    return path


if __name__ == "__main__":
    # Examples assuming path to project is: `/path/to/repo/tim-tam-repo`
    print(get_root_path())
    # `/path/to/repo/tim-tam-repo`

    print(get_static_path("test.txt"))
    # `/path/to/repo/tim-tam-repo/static/test.txt`

    print(get_raw_path("test.txt"))
    # `/path/to/repo/tim-tam-repo/raw/test.txt`

    print(get_processed_path("test.txt"))
    # `/path/to/repo/tim-tam-repo/processed/test.txt`

    print(get_output_path("test.txt"))
    # `/path/to/repo/tim-tam-repo/output/test.txt`

    print(get_output_path("folder1", "folder2", "test.txt"))
    # `/path/to/repo/tim-tam-repo/output/folder1/folder2/test.txt`
