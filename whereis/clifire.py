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
from whereis import Database, Entry, levels, utils
from rich.table import Table
from rich import print
from pathlib import Path
import fire  # type: ignore


def _check_for_db_entries(database: Database) -> bool:
    if not database.entries:
        levels.error("Couldn't find any entries in the database.")
        return False
    else:
        return True


def find(name: str, database_location: str = str(utils.config_folder())) -> None:
    while True:
        try:
            database_location: Path = Path(database_location)  # type: ignore
            database: Database = Database(database_location)  # type: ignore
            if not _check_for_db_entries(database):
                return
            break
        except TypeError:
            levels.error(
                "You aren't supposed to pass '--database-location' like a flag."
            )
            return
        except NotADirectoryError:
            if database_location.exists():  # type: ignore
                levels.error(
                    "The database location exists and is a file. Either,\n"
                    "a.) Remove that file then try again, or\n"
                    "b.) Choose another database location by passing '--database-location <DB_LOCATION>'."
                )
                return
            else:
                levels.info("Database doesn't exist, creating.")
                # noinspection PyUnboundLocalVariable
                database.create()
    table: Table = Table(title="[bold]Config files found")
    table.add_column("Locations")
    table.add_column("Exists")
    table.add_column("Is a file?")
    while True:
        try:
            entry: Entry = next(
                iter([entry for entry in database.entries if entry.name == name])
            )
            break
        except StopIteration:
            levels.error(f"Couldn't find the entry '{name}'.")
            return
        except NotADirectoryError:
            levels.info("Database doesn't exist, creating.")
            database.create()
            continue
    try:
        # noinspection PyUnboundLocalVariable
        for location, exists in entry.locations_exists().items():
            table.add_row(
                f"[green4 bold]{location}",
                f"[green4 bold]{exists}" if exists else f"[red bold]{exists}",
                f"[blue]{location.is_file()}" if exists else "[blue italic]Unknown",
            )
    except KeyError as error:
        levels.error(
            f"Couldn't parse path:\n"
            f"[bold]{error.__class__.__name__}:[/] [italic]{error}"
        )
        return

    print(table)


def main() -> None:
    fire.Fire(find)
