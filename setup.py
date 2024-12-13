#!/usr/bin/env python3
"""Setup for LogFusion."""

import tomllib
from pathlib import Path
from typing import Any

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.install import install


class CustomInstallCommand(install):  # noqa: D101
    def run(self) -> None:  # noqa: D102
        install.run(self)


class CustomDevelopCommand(develop):  # noqa: D101
    def run(self) -> None:  # noqa: D102
        develop.run(self)


class CustomEggInfoCommand(egg_info):  # noqa: D101
    def run(self) -> None:  # noqa: D102
        egg_info.run(self)


def load_pyproject_toml(file_path: Path) -> dict[str, Any]:
    """Load the pyproject.toml file and return its contents as a dictionary."""
    with file_path.open("rb") as f:
        return tomllib.load(f)


with Path("README.md").open(encoding="utf-8") as fh:
    long_description = fh.read()


def main() -> None:
    """Main method."""
    setup(
        name="YapLogger",
        version="0.1.4.1",
        author="Thiago Dias",
        author_email="thiago@thir.info",
        description="A flexible and extensible logging framework for logging, monitoring, and observability.",
        long_description=open("README.md").read(),  # noqa: PTH123, SIM115
        long_description_content_type="text/markdown",
        url="https://github.com/TheAldersonProject/YapLogger",  # Replace with your actual GitHub URL
        packages=find_packages(include=["yaplogger*", "typings*"]),
        package_data={
            "": ["LICENSE", "README.md"],
            "typings": ["**/*.pyi"],  # Include all .pyi files in typings
            "yaplogger": ["py.typed"],  # Marker file for PEP 561 compliance
        },
        classifiers=[
            "Programming Language :: Python",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.12",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Typing :: Typed",  # Added to indicate type support
        ],
        python_requires="~=3.12",
        install_requires=[
            "loguru>=0.7.2",
            "setuptools>=75.6.0",
            "wheel>=0.45.1",
            "types-setuptools>=75.6.0.20241126",
        ],
        cmdclass={
            "install": CustomInstallCommand,
            "develop": CustomDevelopCommand,
            "egg_info": CustomEggInfoCommand,
        },
        zip_safe=False,  # Required for type hints to work properly
    )


if __name__ == "__main__":
    main()
