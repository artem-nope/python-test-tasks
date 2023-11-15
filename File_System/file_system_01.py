import os


if __name__ == '__main__':
    current_dir = os.getcwd()
    for i in os.listdir(current_dir):
        full = os.path.join(current_dir, i)
        print(full, os.path.isdir(full), os.path.isfile(full))