#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open("requirements.txt") as require_file:
    requirements = require_file.readlines()

with open("test-requirements.txt") as test_require_file:
    test_requirements = test_require_file.readlines()

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup(
    name="imcsdk",
    version="0.9.18",
    description="python SDK for Cisco UCS IMC",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Cisco Systems",
    author_email="ucs-python@cisco.com",
    url="https://github.com/ciscoucs/imcsdk",
    packages=[
        "imcsdk",
    ],
    package_dir={"imcsdk": "imcsdk"},
    include_package_data=True,
    install_requires=requirements,
    license="http://www.apache.org/licenses/LICENSE-2.0",
    zip_safe=False,
    keywords="imcsdk",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    tests_require=test_requirements,
    test_suite="nose.collector",
    extras_require={
        "ssl": ["pyOpenSSL"],
        "docs": ["sphinx<1.3", "sphinxcontrib-napoleon", "sphinx_rtd_theme"],
    },
)
