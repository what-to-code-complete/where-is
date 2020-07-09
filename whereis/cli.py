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
import sys


def parser() -> ArgumentParser:
    argparser: ArgumentParser = ArgumentParser(
        "where-is", description="Finds config files."
    )
    argparser.add_argument("-n", "--name", required=True, help="The name of the entry")
    argparser.add_argument(
        "-t", "--type", required=True, help="The type of entry", choices=["config"]
    )

    return argparser


def parse_args(argparser: ArgumentParser, args: List[str] = None) -> Namespace:
    args = args or sys.argv[1:]
    return argparser.parse_args(args)


def main(args: List[str] = None) -> None:
    args = args or sys.argv[1:]
