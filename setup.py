from setuptools import setup
from pybry._generator import generate_lbryd_wrapper
from os import path
from setuptools.command.build_py import build_py

NAME = 'pybry'


class generate_lbryd(build_py):
    def run(self):
        generate_lbryd_wrapper()
        build_py.run(self)


# To read markdown file
this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), mode='r', encoding='utf-8') as outfile:
    long_description=outfile.read()

setup(
    name='pybry',
    url='https://github.com/osilkin98/pybry',
    author='Oleg Silkin',
    author_email='o.silkin98@gmail.com',
    version='1.3.9',
    packages=[NAME, ],
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3',
    cmdclass={'build_py': generate_lbryd}

)
