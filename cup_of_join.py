def join(*args, sep='-'):
    if not args:
        return None
    new_list = []
    for item in args:
        for inner_item in item:
            new_list += [inner_item]
        new_list += [sep]
    new_list = new_list[:-1]
    return new_list


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())