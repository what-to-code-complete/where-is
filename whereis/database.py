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
from typing import List, Dict, Union
from pathlib import Path
import os
from whereis import exceptions, utils


class Entry:
    def __init__(self, name: str, *locations: List[str]) -> None:
        """Initializes an Entry object.

        Args:
            name: The name of an entry.
            *locations: The locations the entry stores.
        """
        self._name = name
        self._locations = locations
        self._database: Database = Database()

    @property
    def name(self) -> str:
        """The name of the entry.

        Returns:
            The name of the entry
        """
        return self._name

    @property
    def locations(self) -> List[Path]:
        """All of the locations an entry has.

        Returns:
            All of the locations an entry has.
        """
        return [Path(os.path.join(*location)) for location in self._locations]

    @property
    def to_dict(self) -> Dict[str, Union[str, List[List[str]]]]:
        """Converts a entry object to a dictionary.

        Returns:
            Converted to dictionary entry object.
        """
        return {
            "name": self.name,
            "locations": self._locations,  # type: ignore
        }

    @property
    def to_json(self) -> str:
        """Converts an entry object to json.

        Returns:
            Converted to json entry object.
        """
        return json.dumps(self.to_dict)

    def add(self) -> None:
        """Adds the entry object to the database.

        Returns:
            Nothing.
        """
        return self._database.add(self)

    def remove(self) -> None:
        """Removes the entry object from the database.

        Returns:
            Nothing.
        """
        return self._database.remove(self)

    def exists(self) -> bool:
        """Checks if the entry object exists.

        Returns:
            True if the entry object exists, else False.
        """
        return self in self._database.entries

    def locations_exists(self) -> Dict[Path, bool]:
        """Does each location exist?

        Returns:
            A dictionary of locations and whether that location exists.
        """
        return {location: location.exists() for location in self.locations}

    def __eq__(self, other) -> bool:
        try:
            return self.name == other.name and self.locations == other.locations
        except ArithmeticError:
            return False

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object: name='{self.name}' locations={self.locations}>"


class Database:
    def __init__(self, location: Path = utils.config_folder()) -> None:
        """Initializes a Database object.

        Args:
            location: The location where the database is. Defaults to the config folder.
        """
        self._location = location

    @property
    def location(self) -> Path:
        """The location where the database is.

        Returns:
            The location where the database is.

        Raises:
            NotADirectoryError: When the database folder doesn't exist.
        """
        if not self._location.is_dir() or not self._location.exists():
            # keyword being 'folder'
            raise NotADirectoryError("The database folder must exist!")
        return self._location

    @property
    def _database(self) -> List[Dict[str, Union[str, List[List[str]]]]]:
        """All of the database in raw.

        Returns:
            A list of dictionaries if the file owning that dictionary's suffix is '.json'.
        """
        return [
            json.loads(entry.read_text())
            for entry in self.location.iterdir()
            if entry.suffix == ".json"
        ]

    @staticmethod
    def _entry_from_json(raw_entry: Dict[str, Union[str, List[List[str]]]]) -> Entry:
        """Converts a json dict to an Entry object.

        Args:
            raw_entry: The entry in json dict.

        Returns:
            An entry object.
        """
        return Entry(raw_entry["name"], *raw_entry["locations"])  # type: ignore

    @property
    def entries(self) -> List[Entry]:
        """A list of all entries.

        Returns:
            A list of entry objects from the database location.
        """
        return [self._entry_from_json(raw_entry) for raw_entry in self._database]

    def add(self, entry: Entry) -> None:
        """Adds an entry to the database.

        Args:
            entry: The entry object.

        Returns:
            Nothing.

        Raises:
            EntryExistsError: If the entry object exists in the database entries.
        """
        if entry in self.entries:
            raise exceptions.EntryExistsError("The database entry exists.")
        new_entry: Path = self.location / f"{entry.name}.json"
        new_entry.write_text(entry.to_json)

    def remove(self, entry: Entry) -> None:
        """Removes an entry from the database.

        Args:
            entry: The entry object.

        Returns:
            Nothing.

        Raises:
            EntryDoesNotExistError: If the entry object doesn't exist in the database entries.
        """
        if entry not in self.entries:
            raise exceptions.EntryDoesNotExistError("The database entry must exist.")
        entry_to_delete: Path = self.location / f"{entry.name}.json"
        entry_to_delete.unlink()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object: location={self.location}>"
