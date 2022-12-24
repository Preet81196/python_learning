

import os

def main():
    '''main function'''
    path = os.getcwd()
    files = os.listdir(path)
    for file in files:
        new_name = file.replace(' ', '_')
        os.rename(file, new_name)

if __name__ == '__main__':
    main()




