import os
from setuptools import setup
from setuptools.command.build_py import build_py
# This should be replaced by setuptools as distutils is deprecated
from distutils.command.clean import clean
from distutils.dir_util import remove_tree

import generator
from template.constants import __version__
from template.constants import NAME


class GenerateAPILocalJSON(build_py):
    """Generates the API from the local JSON file."""

    def run(self):
        argv = ["generator", "docs/api.json"]
        generator.main(argv)
        build_py.run(self)


class GenerateAPIURLJSON(build_py):
    """Generates the API from the JSON file in the online repository."""

    def run(self):
        generator.main(None)
        build_py.run(self)


class Clean(clean):
    def run(self):
        if os.path.exists(NAME):
            remove_tree(NAME)
        clean.run(self)


# To read markdown file
this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, 'README.md'), 'r') as outfile:
    long_description = outfile.read()

setup(
    name=NAME,
    url='https://github.com/osilkin98/PyBRY',
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

