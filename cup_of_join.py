from itertools import chain


def join(*args: list[list[any]], sep: chr = '-') -> list[str]:
    """
    This function receive list of lists and make it one list separate by the sep char.
    :param args: The list of lists.
    :param sep: The char separate between the items, the default sign is '-'.
    :return: The new list.
    """
    if not args:
        return None
    new_list = []
    for item in args:
        new_list = list(chain(new_list, item))
        new_list = list(chain(new_list, sep))
    new_list = new_list[:-1]
    return new_list


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
