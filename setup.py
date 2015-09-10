#!/usr/bin/env python

try:
    from distutils.core import setup
except ImportError as excp:
    from setuptools import setup

import __about__
import os

os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

setup(name='pydot',
      version=__about__.__version__,
      description='Python interface to Graphviz\'s Dot',
      author=__about__.__author__,
      author_email='ero@dkbza.org',
      url='http://code.google.com/p/pydot/',
      license=__about__.__license__,
      keywords='graphviz dot graphs visualization',
      platforms=['any'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      py_modules=['pydot', 'dot_parser'],
      install_requires=['pyparsing', 'setuptools'],
      data_files=[('.', ['LICENSE', 'README'])])
