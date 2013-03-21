#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# setup.py
#
# (c) 2013 Konstantin Sering <konstantin.sering [aet] gmail.com>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2013-02-01 KS
# last mod 2013-03-21 11:29 KS

"""
Compile cython files.

"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

ext_modules = [Extension("simulate_c",
                         ["simulate_c.pyx"],
                         include_dirs=[np.get_include()])]

setup(
  name = 'fast simulate',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)

