
from setuptools import setup, find_packages

setup(
    name='webvis_mods',
    version='0.1',
    license='MIT',

    packages=find_packages(),
    python_requires='>=3.7',

    install_requires = ['loguru', 'hosta'],
    setup_requires = ['pytest-runner'],
    tests_require  = ['pytest'],

    test_suite='tests',
)
