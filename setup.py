#!/usr/bin/env python
from distutils.core import setup
from catkin.package import parse_package_for_distutils

d = parse_package_for_distutils()
d['packages'] = ['genlisp']
d['package_dir'] = {'': 'src'}
d['scripts'] = ['scripts/gen_lisp.py']
d['install_requires'] = ['genmsg']
setup(**d)
