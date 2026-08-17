# pytest-libfaketime [![Latest Version](https://img.shields.io/pypi/v/pytest-libfaketime.svg)](https://pypi.python.org/pypi/pytest-libfaketime)
[python-libfaketime](https://github.com/simon-weber/python-libfaketime) plugin for pytest, with support for [pytest-xdist](https://github.com/pytest-dev/pytest-xdist).

# Installation

```pip install pytest-libfaketime```

# Tests

Run the test suite against the current interpreter with
[uv](https://docs.astral.sh/uv/):

```uv run pytest```

Run it against every supported Python version with
[tox](https://tox.wiki), which needs the
[tox-uv](https://github.com/tox-dev/tox-uv) plugin:

```uv run tox```
