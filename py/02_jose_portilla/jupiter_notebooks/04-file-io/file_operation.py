"""
Read file
"""

import os

ROOT_DIR = f"{os.path.abspath(os.curdir)}/02_jose_portilla/jupiter_notebooks/04-file-io"
print(ROOT_DIR)

myfile = open(f"{ROOT_DIR}/sample.txt", mode="r")
while myfile.closed is False:
    print(myfile.read())
    if myfile.seekable():
        myfile.close()
