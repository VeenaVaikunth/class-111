import os
import shutil

from_dir = './Downloads'
to_dir = './Document_Files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(path)
    print(name)
    print(extension)