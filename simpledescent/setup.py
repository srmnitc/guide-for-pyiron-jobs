#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages, Extension

#with open('README.rst') as readme_file:
#    readme = readme_file.read()

#setup_requirements = ['pytest-runner', ]

#test_requirements = ['pytest>=3', ]

setup(
    author="Sarath Menon",
    author_email='sarathmenon@mailbox.org',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
    ],
    description="a simple 2D potential",
    install_requires=['matplotlib', 'numpy'],
    license="GNU General Public License v3",
    #long_description=readme,
    include_package_data=True,
    keywords='simpledescent',
    name='simpledescent',
    packages=find_packages(include=['simpledescent', 'simpledescent.*']),
    #setup_requires=setup_requirements,
    #test_suite='tests',
    #tests_require=test_requirements,
    #url='https://github.com/srmnitc/pychromatic',
    version='0.0.1',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'simpledescent = simpledescent.minimise_cli:main',
        ],
    }
)