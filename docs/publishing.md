# Publishing Guide

This project can be published as a lightweight Python package if the maintainer decides to distribute the CLI through PyPI.

Publishing is optional. The repository is still usable through editable installation:

```bash
python -m pip install -e .
```

Or through the requirements file:

```bash
python -m pip install -r requirements.txt
```

---

## Package Metadata

Package metadata is defined in:

```text
pyproject.toml
setup.py
```

The package uses:

```text
README.md as the PyPI long description
MIT license
Python >= 3.9
zero core runtime dependencies
optional integration dependencies
optional development dependencies
```

---

## Build Locally

Install development tools:

```bash
python -m pip install -e ".[dev]"
```

Run checks:

```bash
make ci
```

Build the package:

```bash
make build
```

This creates files under:

```text
dist/
```

---

## Check Distribution Files

Before uploading, verify package metadata:

```bash
python -m twine check dist/*
```

---

## Publish Manually

Manual publishing requires a PyPI account and permission to publish the selected package name.

```bash
python -m twine upload dist/*
```

Do not commit PyPI tokens, API keys, or credentials to this repository.

---

## Publish with GitHub Trusted Publishing

The optional workflow in:

```text
.github/workflows/publish.yml
```

uses PyPI Trusted Publishing and does not require storing a PyPI API token in GitHub secrets.

Before using it, configure the project on PyPI and link it to this GitHub repository according to PyPI's Trusted Publishing settings.

Then publish through a GitHub Release or version tag, depending on the workflow trigger you choose to keep.

---

## Versioning Checklist

Before publishing a release:

1. Update `pyproject.toml` version.
2. Update `trendpilot/__init__.py` version if it is exposed there.
3. Update `CHANGELOG.md` with the same version.
4. Run `make ci`.
5. Run `make build`.
6. Run `python -m twine check dist/*`.
7. Create a GitHub release or tag.
