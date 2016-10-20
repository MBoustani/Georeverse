#!/usr/bin/env python
"""
Georeverse
"""

from setuptools import setup, find_packages

INSTALL_REQUIRES = []
TESTS_REQUIRES = []


setup(
    name='Georeverse',
    version=0.2,
    description='Find the best estimate of city, state and country for a given latitude and longitude.',
    author='Mazi Boustani',
    author_email='maziyar_b4@yahoo.com',
    url='https://github.com/MBoustani/Georeverse',
    download_url=('https://github.com/MBoustani/Georeverse/archive/master.zip'),
    packages=find_packages(),
    py_modules=['georeverse'],
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRES,
    extras_require={},
    license='Apache V2',
    keywords='georeverse geosptial latitude longitude opensource free city state country python points',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
