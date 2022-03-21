import os


def thisTheWay():
    # the function read the path and create list of the files start with deep, then print them
    folder_path = input("insert the path to the folder")
    directory_list = os.listdir(folder_path)
    start_with_deep_files = [file_names for file_names in directory_list if file_names.startswith("deep")]
    return start_with_deep_files


files_start_deep = thisTheWay()
print(files_start_deep)
