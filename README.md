<img src="https://github.com/what-to-code-complete/where-is/raw/master/other/logo.png" align="right" width="200" height="178" alt="Logo"/>

# where-is
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI download month](https://img.shields.io/pypi/dm/where-is.svg)](https://pypi.python.org/pypi/where-is/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/where-is.svg)](https://pypi.python.org/pypi/where-is/)
[![PyPI license](https://img.shields.io/pypi/l/where-is.svg)](https://pypi.python.org/pypi/where-is/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/where-is.svg)](https://pypi.python.org/pypi/where-is/)
<p float="left">
  <img src="https://raw.githubusercontent.com/what-to-code-complete/where-is/master/other/find.gif" width="330" height="255"/>
</p>
                                    
> An elegant way of getting configuration files (and folders)


# Getting started
## Prerequisites
- Unix/NT Based OS
- Python>=3.6
- Pip

## Installation
1. Install `where-is` using `pip`.

```bash
$ pip install where-is
```

## Basic Usage
### Get config locations of `grub`
```bash
$ where-is find grub
```
### Add an entry
```bash
$ where-is database --add
```
### Remove an entry
```bash
$ where-is database --remove
```

# More information
For more information and graphics, [see the wiki.](https://github.com/what-to-code-complete/where-is/wiki)

# Built with
- [Rich](https://github.com/willmcgugan/rich): For rich text and beautiful formatting
- [Typer](https://github.com/tiangolo/typer): Used as the argument parser
- [Black](https://github.com/psf/black): Used as the formatter
- [Pipenv](https://github.com/pypa/pipenv): Used as the virtualenv manager

# Acknowledgements
- [joereynolds/what-to-code](https://github.com/joereynolds/what-to-code): For inspiration to make this project
- [Logomakr](https://logomakr.com/): Used to make the logo

# License
This project is licensed under the GNU GPLv3 License - see this [LICENSE.md](https://raw.githubusercontent.com/what-to-code-complete/where-is/master/LICENSE) file for details
