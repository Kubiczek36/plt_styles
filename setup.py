from setuptools import setup, find_packages

setup(
    name='pltstyles',
    version='0.1',
    description='PKG for the plt styles handling',
    author='Jakub Dokulil',
    author_email='jakub.dokulil@imp.ac.at',
    packages=find_packages(),
    install_requires=[
        # list of packages your project depends on
        'matplotlib'
    ],
)
