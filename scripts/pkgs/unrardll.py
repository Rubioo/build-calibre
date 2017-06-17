#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2017, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
from .constants import PREFIX
from .utils import ModifiedEnv, python_build, python_install


def main(args):
    env = {}
    p = PREFIX.replace(os.sep, '/')
    env = dict(
        UNRAR_INCLUDE='{}/include'.format(p),
        UNRAR_LIBDIRS='{0}/lib'.format(p),
    )
    with ModifiedEnv(**env):
        python_build()
    python_install()
