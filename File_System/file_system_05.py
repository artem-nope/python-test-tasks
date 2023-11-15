import pathlib

if __name__ == '__main__':
    cur_file = pathlib.Path(__file__)
    cur_dir = cur_file.parent
    for item in cur_dir.rglob('*.py'):
        print(item)
        print(item.open().read())


