"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['PyCryption.py']
DATA_FILES = [
    ('images', ['images/back.png', 'images/help.png']),
    ('about', ['about/license.txt', 'about/description.txt', 'about/logo.png']),
    'help.html'
]
OPTIONS = {'argv_emulation': True, 'packages': 'wx', 'iconfile': 'app.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)