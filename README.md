# vidtoolz-loudness

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-loudness.svg)](https://pypi.org/project/vidtoolz-loudness/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-loudness?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-loudness/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-loudness/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-loudness/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-loudness/blob/main/LICENSE)

Use EBU R128 Loudness Normalization with ffmpeg

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-loudness
```
## Usage

type ``vid loudness --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-loudness
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
