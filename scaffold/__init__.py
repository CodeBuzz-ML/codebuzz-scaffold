"""
CodeBuzz Scaffold

A modern, extensible CLI for scaffolding software projects.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("codebuzz-scaffold")
except PackageNotFoundError:
    __version__ = "Development"

__author__ = "Advait Muley"
