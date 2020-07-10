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
from argparse import ArgumentParser, Namespace
from typing import List
from whereis import Database, levels, Entry
import sys
from rich.table import Table
from rich import print

_database: Database = Database()


def find_config(name: str):
    table: Table = Table(title="[bold]Config files found")
    table.add_column("Locations")
    table.add_column("Exists")
    table.add_column("Is a file?")
    while True:
        try:
            entry: Entry = next(
                iter([entry for entry in _database.entries if entry.name == name])
            )
            break
        except StopIteration:
            levels.error(f"Couldn't find the entry '{name}'.")
            return
        except NotADirectoryError:
            levels.info("Database doesn't exist, creating.")
            _database.create()
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
        levels.error(f"Couldn't parse path:")
        levels.error(f"[bold]{error.__class__.__name__}:[/] [italic]{error}")
        return

    print(table)


def parser() -> ArgumentParser:
    argparser: ArgumentParser = ArgumentParser(
        "where-is", description="Finds config files."
    )
    argparser.add_argument("-n", "--name", required=True, help="The name of the entry")
    argparser.add_argument(
        "-t",
        "--type",
        help="The type of entry",
        choices=["config"],
        default="config",
        metavar="TYPE",
    )

    return argparser


def parse_args(argparser: ArgumentParser, args: List[str] = None) -> Namespace:
    args = args or sys.argv[1:]
    return argparser.parse_args(args)


def main(args: List[str] = None) -> None:
    args = args or sys.argv[1:]
    arguments: Namespace = parse_args(parser(), args)
    return find_config(arguments.name)
