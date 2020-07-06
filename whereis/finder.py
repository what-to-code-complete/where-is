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
import json
from typing import List, Union, Dict
from pathlib import Path


class Entry:
    def __init__(self, raw: Dict[str, Union[str, List[str]]]) -> None:
        self.raw = raw


class Database:
    def __init__(self, location: Path) -> None:
        """Database initializer.

        Args:
            location: The location where the database is stored.
        """
        self.location = location
        self._check()

    def _check(self) -> None:
        if not self.location.exists():
            raise FileNotFoundError(f"Location '{self.location}' does not exist.")
        if not self.location.is_dir():
            raise NotADirectoryError(f"Location '{self.location}' must be a folder, not a file.")
