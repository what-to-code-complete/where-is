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
from whereis import Database
import fire
from typing import List


class EntryCLI:
    def __init__(self) -> None:
        self._database: Database = Database()

    def add(self, name: str, *locations: List[str]) -> None:
        """Adds an entry to the database.

        Args:
            name: The name of the entry to add.
            *locations: The locations to add to the database.

        Returns:
            Nothing.
        """
        print(name, locations)


class FindCLI:
    pass


class Nest:
    def __init__(self) -> None:
        self.entry: EntryCLI = EntryCLI()
        self.find: FindCLI = FindCLI()


def main() -> None:
    fire.Fire(Nest())
