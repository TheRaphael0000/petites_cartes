#!/usr/bin/env python
import os
import setuptools


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="petites_cartes",
    version="0.0.1",
    author="Raphaël Margueron",
    author_email="raphael.margueron@gmail.com",
    description=(""),
    license="",
    keywords="",
    url="https://github.com/TheRaphael0000/petites_cartes",
    packages=["petites_cartes"],
    long_description=read("README.md"),
    classifiers=[],
    install_requires=read("requirements.txt"),
    entry_points={
        "console_scripts": [
            "cartes=petites_cartes.__main__:main"
        ]
    },
)
