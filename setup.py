# where-is: Finds config files.
# Copyright (C) 2020 ALinuxPerson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from typing import List, Dict
import setuptools
import pathlib

REQUIRED: List[str] = ["rich==3.1.0", "fire==0.3.1"]
EXTRAS: Dict[str, List[str]] = {"dev": ["mypy==0.782"]}

setuptools.setup(
    name="where-is",
    version=pathlib.Path("VERSION").read_text().strip(),
    description="Finds config files.",
    long_description=pathlib.Path("README.md").read_text().strip(),
    author="ALinuxPerson",
    author_email="micheal02052007@gmail.com",
    python_requires=">=3.6.0",
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    entry_points={"console_scripts": ["where-is=whereis.__main__:main"]},
    include_package_data=True,
    license="GNU GPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
    ],
)
