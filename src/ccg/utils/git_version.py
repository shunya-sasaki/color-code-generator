"""This module define GitVersion class."""

import re
import shutil
import subprocess
from importlib.metadata import version as prodcut_version
from importlib.resources import as_file
from importlib.resources import files
from pathlib import Path


class GitVersion:
    """Class to manage git operations."""

    @classmethod
    def _execute(cls, args: list[str]) -> str:
        out = subprocess.run(
            args=args, capture_output=True, text=True, check=True
        ).stdout.strip()
        return out

    @classmethod
    def package_name(cls) -> str:
        """Return the package name."""
        origin_path = Path(__file__)
        parents = origin_path.parents
        package_name = origin_path.name
        is_package_found = False
        for parent in parents:
            if parent.name in ["src", "site-packages"]:
                is_package_found = True
                break
            else:
                package_name = parent.name
        if not is_package_found:
            raise RuntimeError(
                "Package directory should be within `src` "
                + "or `site-packages` directory."
            )
        return package_name

    @classmethod
    def is_product(cls) -> bool:
        """Check if the package is a product."""
        package_name = cls.package_name()
        traverse = files(package_name)
        context_manager = as_file(traverse)
        with context_manager as path:
            package_path = Path(path)
        parent = package_path.parent.name
        if parent == "site-packages":
            is_product = True
        else:
            is_product = False
        return is_product

    @classmethod
    def git_available(cls) -> bool:
        """Check if git is available in the system."""
        path = shutil.which("git")
        return path is not None

    @classmethod
    def version(cls) -> str:
        """Return the current git version."""
        version = "unknown"
        if cls.is_product():
            version = cls._version_from_metadata()
        if version == "unknown" and cls.git_available():
            out = cls._execute(["git", "describe", "--tags", "--dirty"])
            describes = out.split("-")
            semantic_version = re.sub(r"^v", "", describes[0])
            commit_count = int(describes[1])
            commit_hash = re.sub(r"^g", "", describes[2])
            is_dirty = describes[-1] == "dirty"
            major, minor, patch = semantic_version.split(".")
            if commit_count == 0 and not is_dirty:
                version = f"{major}.{minor}.{patch}"
            elif is_dirty:
                version = (
                    f"{major}.{minor}.{patch}"
                    + f".post{commit_count}.dev0+{commit_hash}"
                )
            else:
                version = (
                    f"{major}.{minor}.{patch}"
                    + f".post{commit_count}+{commit_hash}"
                )
        return version

    @classmethod
    def _version_from_metadata(cls) -> str:
        """Get the version from the package metadata."""
        package_name = cls.package_name()
        try:
            version = prodcut_version(package_name)
        except Exception as e:
            version = "unknown"
        return version
