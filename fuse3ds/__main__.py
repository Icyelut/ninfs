#!/usr/bin/env python3

from importlib import import_module
from sys import exit, argv, path
from os.path import basename, dirname, realpath

try:
    from . import __version__
except ImportError:
    try:
        from __init__ import __version__
    except ImportError:
        __version__ = '<unset>'

mount_types = ('cci', 'cdn', 'cia', 'exefs', 'nand', 'ncch', 'romfs', 'sd')
mount_aliases = {'3ds': 'cci', 'cxi': 'ncch', 'cfa': 'ncch', 'app': 'ncch'}

print('fuse-3ds {} - https://github.com/ihaveamac/fuse-3ds'.format(__version__))

def exit_print_types():
    print('Please provide a mount type as the first argument.')
    print(' ', ', '.join(mount_types))
    exit(1)

def mount(mount_type: str) -> int:
    # noinspection PyProtectedMember
    from mount._common import windows
    if windows:
        from ctypes import windll
        if windll.shell32.IsUserAnAdmin():
            print('- Note: This should *not* be run as an administrator.',
                  '- The mount will not be normally accessible.',
                  '- This should be run from a non-administrator command prompt or PowerShell prompt.', sep='\n')
    else:
        try:
            from os import getuid
            if getuid() == 0:  # 0 == root on macos and linux
                print('- Note: This should *not* be run as root.',
                      '- The mount will not be normally accessible by other users.',
                      '- This should be run from a non-root terminal.',
                      '- If you want root to be able to access the mount,',
                      '-   you can add `-o allow_root` to the arguments.',
                      sep='\n')
        except (AttributeError, ImportError):
            pass
    if mount_type not in mount_types and mount_type not in mount_aliases:
        exit_print_types()

    module = import_module('mount.' + mount_aliases.get(mount_type, mount_type))
    return module.main()

def main():
    path.append(dirname(realpath(__file__)))
    exit(mount(basename(argv[0])[6:].lower()))

if __name__ == '__main__':
    if len(argv) < 2:
        exit_print_types()

    # path fun times
    path.append(dirname(realpath(__file__)))
    exit(mount(argv.pop(1).lower()))