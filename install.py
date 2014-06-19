#!/usr/bin/env python
from __future__ import print_function

import os
import shutil

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    files = ['cde', 'cde-exec']
    dest = os.path.join(os.environ['HOME'], '.local', 'bin')
    for f in files:
        ffrom = os.path.join(base, f)
        fto = dest
        print("Copying {0} to {1}".format(ffrom, fto))
        shutil.copy(ffrom, fto)

if __name__ == '__main__':
    main()
