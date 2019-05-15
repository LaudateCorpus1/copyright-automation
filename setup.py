#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from __future__ import with_statement

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import copyright_automation


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as changelog_file:
    changelog = changelog_file.read()

requirements = []

setup_requirements = ["pytest-runner",]

test_requirements = ["pytest", "pytest-cov", "coverage",]

setup(
    author=copyright_automation.__author__,
    author_email=copyright_automation.__email__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Check or Updates source files using given copyright notice and end year.",
    entry_points={
        "console_scripts": [
            "copyright-automation=copyright_automation.cli:main",
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="copyright_automation",
    name=copyright_automation.__project__,
    packages=find_packages(include=["copyright_automation"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/tomtom-international/copyright-automation",
    version=copyright_automation.__version__,
    zip_safe=False,
)
