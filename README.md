# Legacy Python Demo

This repository is a small test project for validating a Python version migration workflow.

It is designed to be used with an AAVA Python migration MVP workflow that:

1. Clones a GitHub repository.
2. Inspects Python files and configuration.
3. Detects Python version references.
4. Finds migration risks.
5. Runs basic validation tests.
6. Produces a migration report.

## Intentional Migration Issue

`app.py` intentionally uses:

```python
from distutils.version import LooseVersion
```

This is included so migration tools can detect `distutils` and `LooseVersion` usage and recommend replacing it with:

```python
from packaging.version import Version
```

## Target Migration Scenario

Source Python version: 3.11
Target Python version: 3.14

## Run Tests

```shell
pip install -r requirements.txt
pytest
```