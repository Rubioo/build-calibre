#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2016, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import (unicode_literals, division, absolute_import,
                        print_function)
import os
import shutil

from .constants import iswindows, PYTHON, build_dir, SW, PREFIX
from .utils import run


if iswindows:
    def main(args):
        run(PYTHON, 'setup.py', 'fetch', '--all', '--missing-checksum-ok', 'build', 'install', '--root', build_dir())
        os.rename(os.path.join(build_dir(), os.path.basename(SW), os.path.basename(PREFIX), 'private'), os.path.join(build_dir(), 'private'))
        shutil.rmtree(os.path.join(build_dir(), os.path.basename(SW)))
