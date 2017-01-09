# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

setup(
    name='pytimeout',
    version='0.0.1',
    author='Tsukasa NAKATANI',
    url='https://github.com/tsukachu/pytimeout',
    license='MIT',
    description='Minimal timeout handling to developers.',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Education :: Testing',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
)
