"""
This is a setup.py script generated by py2applet

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

APP = ['PCExtractorApp.py']
DATA_FILES = ['GNU GENERAL PUBLIC LICENSE.txt']
OPTIONS = {
	'iconfile': 'icon.icns'
}

setup(
    app=APP,
    name="Pharmacists Clinic Data Extractor",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
