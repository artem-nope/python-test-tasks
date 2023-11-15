import os


def spider(start_dir, ext='.py'):
    for i in os.walk(start_dir):
        files = i[2]
        for f in files:
            if f.endswith(ext):
                print(f)
                full = os.path.join(i[0], f)
                print(open(full).read())



if __name__ == '__main__':
    current_dir = os.getcwd()
    spider(current_dir)