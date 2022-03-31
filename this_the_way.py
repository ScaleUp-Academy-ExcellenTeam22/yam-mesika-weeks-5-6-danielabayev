import os


def this_the_way(path: str) -> list[str]:
    """
    This function get from the user path to folder and return all the files start with the word "deep".
    :param path: The path to the folder to check.
    :return: List of the files start with deep.
    """
    return [file_names for file_names in os.listdir(path) if file_names.startswith("deep")]


if __name__ == "__main__":
    folder_path = input("insert the path to the folder")
    files_start_deep = this_the_way(folder_path)
    print(files_start_deep)
