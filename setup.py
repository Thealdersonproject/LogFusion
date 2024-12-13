#!/usr/bin/env python3
"""Setup for LogFusion."""

import tomllib
from pathlib import Path
from typing import Any

from setuptools import setup


def load_pyproject_toml(file_path: Path) -> dict[str, Any]:
    """Load the pyproject.toml file and return its contents as a dictionary."""
    with file_path.open("rb") as f:
        return tomllib.load(f)


with Path("README.md").open(encoding="utf-8") as fh:
    long_description = fh.read()


def main() -> None:
    """Main method."""
    # Load the pyproject.toml file
    pyproject_content = load_pyproject_toml(Path("pyproject.toml"))

    # Extract necessary information from the pyproject.toml file
    project_info = pyproject_content["project"]

    setup(
        # Basic project information
        name=project_info["name"],
        version=project_info["version"],
        author=project_info["authors"][0],
        author_email=project_info["authors"][0],
        description=project_info["description"],
        long_description=long_description,
        long_description_content_type="text/markdown",
        # Project URLs
        url="https://github.com/TheAldersonProject/YapLogger",
        # Package discovery
        package_dir={"yaplogger": ""},
        # Package data
        include_package_data=True,
        package_data={
            "": ["*.json", "*.yaml", "*.pyi"],
        },
        # Dependencies
        python_requires=project_info["requires-python"],
        install_requires=project_info["dependencies"],
        # Classifiers help users find your project
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            f"Programming Language :: Python :: {project_info['requires-python']}",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        # Additional metadata
        platforms=["any"],
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
