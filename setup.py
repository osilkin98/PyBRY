from distutils.core import setup
from distutils.command.build_py import build_py
from generator import generate_lbryd_wrapper

NAME = 'pybry'

class generate_lbryd(build_py):
    def run(self):
        generate_lbryd_wrapper()
        build_py.run()


setup(
    name='pybry',
    version='1.2',
    packages=[NAME, ],
    license='MIT License',
    long_description=open('README.md', mode='r').read(),
    cmdclass={'build_py': generate_lbryd}

)
