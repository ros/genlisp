#!/usr/bin/env python

from setuptools import setup

import sys
sys.path.insert(0, 'src')

import re
search = re.search(r'Version\:\s*(\d+\.\d+\.\d+)',open('stack.yaml').read())
if not search:
    print >>sys.stderr, 'You must have a Version field in your stack.yaml'
    sys.exit(-1)
__version__ = search.groups()[0]

#from genlisp import __version__

setup(name='genlisp',
      version= __version__,
      packages=['genlisp'],
      package_dir = {'':'src'},
      install_requires=['genmsg'],
      scripts = ['scripts/gen_lisp.py'],
      author = "Bhaskara Marthi",
      author_email = "bhaskara@willowgarage.com",
      url = "http://www.ros.org/wiki/genlisp",
      download_url = "http://pr.willowgarage.com/downloads/genlisp/",
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License" ],
      description = "ROS msg/srv Lisp generation",
      long_description = """\
Library and scripts for generating ROS message data structures in LISP.
""",
      license = "BSD"
      )
