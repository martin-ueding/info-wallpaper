#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>

from setuptools import setup, find_packages

__docformat__="restructuredtext en"

setup(
    author = "Martin Ueding",
    author_email = "dev@martin-ueding.de",
    description = "Generates wallpapers with hardware information",
    license = "GPL2",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",

    ],
    name = "info-wallpaper",
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'info-wallpaper = infowallpaper.__init__:main',
        ],
    },
    install_requires=[
        'PIL',
    ],
    url = "https://github.com/martin-ueding/info-wallpaper",
    download_url="http://martin-ueding.de/download/info-wallpaper/",
    version = "1.0",
)
