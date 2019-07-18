#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yuval tisf Nativ'
__license__ = 'GPLv3'
__copyright__ = '2018, Yuval tisf Nativ'

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


required = [
    'requests>=1.0.0',
    'impacket>=0.9.0',
    'slackclient',
    'progressbar',
    'numpy',
    'Pillow',
    'pytube',
    'PyCrypto',
    'base58',
    'luhn',
    'names',
    'faker',
]
			
			# note: attempting to install "zlib" breaks "pip install", as zlib is not a pip, but a system package
			# proof: https://stackoverflow.com/a/6169902
			# Update: Turns out the same story for: "urllib2", "ftplib" and "hashlib". All are pre-installed with python, and installing them with pip after breaks "pip install PyExfil" flow
			
			# note: PIL is (sadly) dead, and as part of it, there is no weay to install PIL onto Ubuntu
			# but the workaround is simple! Just replace "PIL" with "Pillow"
			# and luckily, no need to modify import for this particular project
			# proof: https://stackoverflow.com/a/41326447
			
            # Todo: Set that urllib2 is not installed from pip for Python3


if __name__ == '__main__':
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    long_desc = open('README.md').read() + '\n\n' + open('LICENSE.md').read()

    setup(name='PyExfil',
        maintainer=__author__,
        maintainer_email='yuval@morirt.com',
        description="""PyExfil: Python communication library over non-standard channels.""",
        license=__license__,
        url='https://www.github.com/ytisf/pyexfil',
        version="1.0 RC1",
        download_url='https://www.github.com/ytisf/pyexfil',
        long_description=long_desc,
        install_requires=required,
        platforms='any',
        packages=find_packages(),
        classifiers=(
                'Development Status :: 3 - Beta',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                'Topic :: Software Development',
                'Topic :: Scientific/Engineering',
                'Environment :: Console',
                'Operating System :: Microsoft :: Windows',
                'Operating System :: POSIX',
                'Operating System :: Unix',
                'Operating System :: MacOS',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.7',)
        )
