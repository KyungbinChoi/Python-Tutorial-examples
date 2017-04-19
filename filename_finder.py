import os
import sys

try:
    directory_path = sys.argv[1]
    word = sys.argv[2]
    for (path, dir, files) in os.walk(directory_path):
        for filename in files:
            name = os.path.splitext(filename)[0]
            if name.find(word) != -1: #if word in name:
                print("%s/%s" %(path, filename))
except PermissionError as Error1:
    pass


