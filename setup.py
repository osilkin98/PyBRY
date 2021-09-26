from setuptools import setup
from generator import generate_lbryd_wrapper
from os import path
from setuptools.command.build_py import build_py
# This should be replaced by setuptools as distutils is deprecated
from distutils.command.clean import clean
from distutils.file_util import copy_file
from pybry import __version__

NAME = 'pybry'


class GenerateAPILocalJSON(build_py):
    """Generates the API from the local JSON file."""

    def run(self):
        generate_lbryd_wrapper(doc="docs/api.json")
        build_py.run(self)


class GenerateAPIURLJSON(build_py):
    """Generates the API from the JSON file in the online repository."""

    def run(self):
        generate_lbryd_wrapper()
        build_py.run(self)


class Clean(clean):
    def run(self):
        copy_file("pybry/__lbryd_api__.py", "pybry/lbryd_api.py")
        clean.run(self)


# To read markdown file
this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), mode='r', encoding='utf-8') as outfile:
    long_description = outfile.read()

setup(
    name=NAME,
    url='https://github.com/belikor/PyBRY',
    author='Oleg Silkin, Beliko R',
    author_email='o.silkin98@gmail.com',
    version=__version__,
    packages=[NAME],
    license='MIT License',
    description="A Binded Python API for the LBRYD and LBRYCRD network",
    long_description=long_description,
    long_description_content_type='text/markdown',
    requires=['yapf'],
    python_requires='>=3',
    cmdclass={'build_py': GenerateAPILocalJSON,
              'build_local': GenerateAPILocalJSON,
              'build_online': GenerateAPIURLJSON,
              'clean': Clean}
)

