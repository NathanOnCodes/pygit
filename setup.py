from setuptools import setup

setup(
    version='0.0.1',
    packages=['pygit'],
    entry_points={
        'console_scripts': [
            'pygit = pygit.cli:main'
        ]
    }
)