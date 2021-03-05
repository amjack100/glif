#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


requirements = [
    "Click>=7.0",
]

setup_requirements = []

test_requirements = []

setup(
    author="Andy Jackson",
    author_email="amjack100@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Generates a gif from image files of a glob pattern",
    entry_points={
        "console_scripts": [
            "glob_to_gif=glob_to_gif.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords="glob_to_gif",
    name="glob_to_gif",
    packages=find_packages(include=["glob_to_gif", "glob_to_gif.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/amjack100/glob_to_gif",
    version="0.1.0",
    zip_safe=False,
)
