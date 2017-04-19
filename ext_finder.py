import os
import sys

try:
    directory_path = sys.argv[1]
    file_ext = sys.argv[2]
    for (path, dir, files) in os.walk(directory_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.'+ file_ext:
                print("%s/%s" %(path, filename))
except PermissionError as Error1:
    pass


