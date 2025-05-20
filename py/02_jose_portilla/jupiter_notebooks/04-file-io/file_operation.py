"""
Read file
"""

import os

ROOT_DIR = (
    f"{os.path.abspath(os.curdir)}/02_jose_portilla" "/jupiter_notebooks/04-file-io/"
)

print()
with open(f"{ROOT_DIR}/sample.txt", mode="r", encoding="utf-8") as my_file:
    while my_file.closed is False:
        print(my_file.read())
        if my_file.seekable():
            my_file.close()
