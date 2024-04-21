from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Testing tools'
LONG_DESCRIPTION = 'A package that contains softwares to help testers.'

# Setting up
setup(
    name="Easy-test-tools",
    version=VERSION,
    author="Achref Znaidia",
    author_email="<achref.znaidia@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['flet'],
    keywords=['python', 'test', 'testing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)