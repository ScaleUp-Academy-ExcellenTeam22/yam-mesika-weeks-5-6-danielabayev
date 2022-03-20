import os


# the function read the path and create list of the files start with deep, then print them
def thisTheWay():
    folder_path = input("insert the path to the folder")
    directory_list = os.listdir(folder_path)
    only_deep = [f for f in directory_list if f.startswith("deep")]
    print(only_deep)


thisTheWay()
