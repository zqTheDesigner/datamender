from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='datamender',
    version='0.0.0',
    author='zqthedesigner', 
    author_email='zqthedesigner@gmail.com',
    packages=find_packages(),
    package_data={'': ['datamender/datasets/data/*']},
    long_description=open('README.md').read()
)