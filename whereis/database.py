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
from typing import List, Dict, Union, Optional, TextIO
from pathlib import Path
import os
from whereis import exceptions


class Entry:
    def __init__(self, name: str, *locations: List[str]) -> None:
        self._name = name
        self._locations = locations

    @property
    def name(self) -> str:
        return self._name

    @property
    def locations(self) -> List[Path]:
        return [Path(os.path.join(*location)) for location in self._locations]

    @property
    def to_dict(self) -> Dict[str, Union[str, List[List[str]]]]:
        return {
            "name": self.name,
            "locations": self._locations,  # type: ignore
        }

    @property
    def to_json(self) -> str:
        return json.dumps(self.to_dict)

    def add(self) -> None:
        pass

    def remove(self) -> None:
        pass

    def exists(self) -> bool:
        pass

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.locations == other.locations

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object: name={self.name} locations={self.locations}>"


class Database:
    def __init__(self, location: Path) -> None:
        self._location = location

    @property
    def location(self) -> Path:
        if not self._location.is_dir() or not self._location.exists():
            # keyword being 'folder'
            raise NotADirectoryError("The database folder must exist!")
        return self._location

    @property
    def _database(self) -> List[Dict[str, Union[str, List[List[str]]]]]:
        return [json.loads(entry.read_text()) for entry in self.location.iterdir()]

    @staticmethod
    def _entry_from_json(raw_entry: Dict[str, Union[str, List[List[str]]]]) -> Entry:
        return Entry(raw_entry["name"], *raw_entry["locations"])  # type: ignore

    @property
    def entries(self) -> List[Entry]:
        return [self._entry_from_json(raw_entry) for raw_entry in self._database]

    def add(self, entry: Entry) -> None:
        if entry in self.entries:
            raise exceptions.EntryExistsError("The database entry exists.")
        new_entry: Path = self.location / f"{entry.name}.json"
        new_entry.write_text(entry.to_json)

    def remove(self, entry: Entry) -> None:
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object: location={self.location}>"
