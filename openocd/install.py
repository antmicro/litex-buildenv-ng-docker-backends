#!/usr/bin/env python

import os
from platform import system as sys


def create_path(path):
    if not os.path.isdir(path):
        print(f"# Creating path {path}")
        os.makedirs(path, exist_ok=True)

def copy_executable(src, dest_dir):
    _, filename = os.path.split(src)
    dest = dest_dir + "/" + filename
    with open(src, 'rb') as data_in, open(dest, 'wb') as data_out:
        data_out.write(data_in.read())
    print(f"# File {src} coppied to {dest_dir}")
    if sys() == "Windows":
        with open(dest + ".cmd", 'w') as cmdfile:
            cmdfile.write(f"@echo off\npython {dest}")
            print("# System identified as Windows. Created addtional .cmd file to enable running by filename")
    else:
        os.chmod(dest, 0o555)

def setup(*args):
    if len(args) == 2:
        executable, target_dir = args
    if len(args) == 1:
        target_dir = args[0]
        executable = os.path.dirname(os.path.realpath(__file__)) + "/openocd"
    create_path(target_dir)
    copy_executable(executable, target_dir)


if __name__ == "__main__":
    from sys import argv, exit

    try:
        target_dir = argv[1]
    except IndexError:
        print("Not enough arguments. Please provide args:\n\t<src> <target_dir>")
        exit(1)

    setup(target_dir)
