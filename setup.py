#!/usr/bin/env python3
"""Setup for LogFusion."""

import tomllib
from pathlib import Path
from typing import Any

from setuptools import find_packages, setup


def load_pyproject_toml(file_path: Path) -> dict[str, Any]:
    """Load the pyproject.toml file and return its contents as a dictionary."""
    with file_path.open("rb") as f:
        return tomllib.load(f)


def main() -> None:
    """Main method."""
    # Load the pyproject.toml file
    pyproject_content = load_pyproject_toml(Path("pyproject.toml"))

    # Extract necessary information from the pyproject.toml file
    project_info = pyproject_content["project"]

    setup(
        name=project_info["name"],
        version=project_info["version"],
        description=project_info["description"],
        author=project_info["authors"][0],
        author_email=project_info["authors"][0],
        url=project_info.get("url", "https://github.com/Thealdersonproject/LogFusion"),
        packages=find_packages(),
        install_requires=project_info["dependencies"],
        classifiers=project_info["classifiers"],
        python_requires=project_info["requires-python"],
        include_package_data=True,
        package_data={"typings": ["*.pyi"]},
    )


if __name__ == "__main__":
    main()
