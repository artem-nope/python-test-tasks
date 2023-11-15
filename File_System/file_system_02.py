import os


def spider(start_dir, ext='.py'):
    for i in os.listdir(start_dir):
        full = os.path.join(start_dir, i)
        # print(full, os.path.isdir(full), os.path.isfile(full))
        if os.path.isdir(full):
            # print(full)
            spider(full)
        elif full.endswith(ext):
            print()
            print(' * ' * 10)
            print(full)
            print(' * ' * 10)
            content = open(full, 'r').read()
            print(content)



if __name__ == '__main__':
    current_dir = os.getcwd()
    spider(current_dir)