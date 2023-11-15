import pathlib


if __name__ == '__main__':
    cur_file = pathlib.Path(__file__)
    print(__file__, type(__file__))
    print(cur_file, type(cur_file))
    print(cur_file.is_file())
    print(cur_file.suffix)

    cur_dir = cur_file.parent
    print(cur_dir, type(cur_dir))

    cur_file1 = cur_dir / 'file_system_07.py'
    print(cur_file1)
    print(cur_file1.exists())

    