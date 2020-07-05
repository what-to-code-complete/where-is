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

from rich.console import Console
import sys

_console: Console = Console(file=sys.stderr)


def info(message: str, no_icon: bool = False) -> None:
    """Prints out an info message.

    Args:
        message: The message.
        no_icon: Does the message have an icon or not?

    Returns:
        Nothing.
    """
    for line in message.splitlines():
        _console.print(f" [dark_blue]{'' if no_icon else '[[🛈]]'} [blue]{line}")


def success(message: str, no_icon: bool = False) -> None:
    """Prints out a success message.

    Args:
        message: The message.
        no_icon: Does the message have an icon or not?

    Returns:
        Nothing.
    """
    for line in message.splitlines():
        _console.print(f" [dark_green]{'' if no_icon else '[[✓]]'} [green4]{line}")


def warn(message: str, no_icon: bool = False) -> None:
    """Prints out a warning message.

    Args:
        message: The message.
        no_icon: Does the message have an icon or not?

    Returns:
        Nothing.
    """
    for line in message.splitlines():
        _console.print(f" [yellow]{'' if no_icon else '[[⚠]]'} [yellow3]{line}")


def error(message: str, no_icon: bool = False) -> None:
    """Prints out an error message.

    Args:
        message: The message.
        no_icon: Does the message have an icon or not?

    Returns:
        Nothing.
    """
    for line in message.splitlines():
        _console.print(f" [dark_red]{'' if no_icon else '[[✗]]'} [red]{line}")


def debug(message: str) -> None:
    """Prints out a debug message.

    Args:
        message: The message.

    Returns:
        Nothing.
    """
    for line in message.splitlines():
        _console.log(f"[cyan]🔍 {line}")
