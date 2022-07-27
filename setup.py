#!/usr/bin/env python

from setuptools import setup

"""
We can't just import __version__ without installed dependencies
"""

version_info = {}
with open("vxdb/__version__.py") as f:
    exec(f.read(), version_info)

setup(
    name="vxdb",
    version=version_info["__version__"],
    description="MWDB API bindings for Python",
    author="psrok1",
    packages=["vxdb", "vxdb.api", "vxdb.cli", "vxdb.cli.formatters"],
    package_data={"vxdb": ["py.typed"]},
    url="https://github.com/backchannelinc/vxdb",
    python_requires=">=3.7",
    install_requires=["requests", "keyring>=18.0.0"],
    extras_require={
        "cli": [
            "click>=7.0",
            "click-default-group",
            "beautifultable>=1.0.0",
            "humanize>=0.5.1",
        ]
    },
    entry_points={"console_scripts": ["vxdb = vxdb.cli:main [cli]"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
