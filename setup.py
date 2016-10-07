import os
from setuptools import setup

setup(
    name = "vixenconverter",
    version = "0.0.1",
    author = "Ryan Fredlund <fredl027>, Kelly Larson <lars4986>",
    description = ("Converts *.vix to Proton format"),
    license = "MIT",
    url = "https://github.com/teslaworksumn/proton-vixen-converter",
    packages=['vixenconverter', 'tests'],
    install_requires=['docopt']
)
