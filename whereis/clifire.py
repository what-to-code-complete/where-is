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
from whereis import Database, Entry, levels, exceptions
import fire
from typing import List


class EntryCLI:
    def __init__(self) -> None:
        self._database: Database = Database()

    @staticmethod
    def _comma_delimit_to_list(comma_delimit: str) -> List[str]:
        """Converts a comma-delimited string to a list fit for being passed to Entry.*locations.

        Args:
            comma_delimit: The comma-delimited string.

        Returns:
            A converted comma-delimited string.
        """
        return comma_delimit.split(",")

    def add(self, name: str, *locations: str) -> None:
        """Adds an entry to the database.

        Notes:
            Note that you SHOULD NOT use this method to add entries to the database. You should use the better method,
            create the entry from scratch using a JSON.

        Args:
            name: The name of the entry to add.
            *locations: The locations to add to the database.

        Returns:
            Nothing.
        """
        converted_locations: List[List[str]] = [
            self._comma_delimit_to_list(location) for location in locations
        ]
        entry: Entry = Entry(name, *converted_locations)
        entry.database = self._database
        try:
            entry.add()
        except exceptions.EntryExistsError as error:
            levels.error(f"The specified entry exists: {error}")
            return
        levels.success(f"Successfully added entry to database.")


class FindCLI:
    pass


class Nest:
    def __init__(self) -> None:
        self.entry: EntryCLI = EntryCLI()
        self.find: FindCLI = FindCLI()


def main() -> None:
    fire.Fire(Nest())
