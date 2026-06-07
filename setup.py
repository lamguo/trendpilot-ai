"""Legacy setuptools entry point.

Modern installs should use pyproject.toml, but this tiny setup.py keeps older
pip/setuptools workflows from failing unexpectedly.
"""

from setuptools import setup

setup()
