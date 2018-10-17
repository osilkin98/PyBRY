from distutils.core import setup
from distutils.command.build_py import build_py
from generator import generate_lbryd_wrapper


NAME = 'pybry'


class generate_lbryd(build_py):
    def run(self):
        generate_lbryd_wrapper()
        build_py.run(self)


setup(
    name='pybry',
    url='https://github.com/osilkin98/pybry',
    author='Oleg Silkin',
    author_email='o.silkin98@gmail.com',
    version='1.2.1',
    packages=[NAME, ],
    license='MIT License',
    long_description=open('README.md', mode='r').read(),
    python_requires='>=3',
    cmdclass={'build_py': generate_lbryd}

)
