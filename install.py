import os
import shutil

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    files = ['cde']
    dest = os.path.join(os.environ['HOME'], '.local', 'bin')
    for f in files:
        shutil.copy(os.path.join(base, f), dest)
