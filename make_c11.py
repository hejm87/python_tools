#!/usr/bin/python3

import os
import sys

if len(sys.argv) != 2:
    sys.exit()
file = sys.argv[1]
bin = file.split(".")[0]
os.system(f"g++ --std=c++11 -g -o {bin} {file}")
