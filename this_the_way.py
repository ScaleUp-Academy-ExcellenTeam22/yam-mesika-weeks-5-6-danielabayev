import os


def this_the_way() -> list[str]:
    """
    This function get from the user path to folder and return all the files start with the word "deep".
    :return: list of the files start with deep.
    """
    # the function read the path and create list of the files start with deep, then print them
    folder_path = input("insert the path to the folder")
    directory_list = os.listdir(folder_path)
    start_with_deep_files = [file_names for file_names in directory_list if file_names.startswith("deep")]
    return start_with_deep_files


if __name__ == "__main__":
    files_start_deep = this_the_way()
    print(files_start_deep)
