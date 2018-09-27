import os

dirname = '/Users/taosang1992/practice/py/testfolder'

try:
    os.makedirs(dirname)
except OSError:
    if os.path.exists(dirname):
        pass
    else:
        raise