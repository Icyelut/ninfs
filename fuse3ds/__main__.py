#!/usr/bin/env python3

from importlib import import_module
from sys import exit, argv
from os.path import basename

from . import __version__

mount_types = ('cci', 'cdn', 'cia', 'nand', 'ncch', 'romfs', 'sd')

print('fuse-3ds {} - https://github.com/ihaveamac/fuse-3ds'.format(__version__))

def exit_print_types():
    print('Please provide a mount type as the first argument.')
    print(' ', ', '.join(mount_types))
    exit(1)

def mount(mount_type: str) -> int:
    if mount_type not in mount_types:
        exit_print_types()

    module = import_module('fuse3ds.mount.' + mount_type)
    return module.main()

def main():
    exit(mount(basename(argv[0])[6:].lower()))

if __name__ == '__main__':
    if len(argv) < 2:
        exit_print_types()

    exit(mount(argv.pop(1).lower()))
