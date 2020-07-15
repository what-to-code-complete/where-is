"""Testing for whereis.core"""
from whereis import Database, Entry, exceptions
import pytest  # type: ignore
import os
from pathlib import Path
from typing import Dict, Union, List
import string
import random


def generate_random_string(max_chars: int = 8) -> str:
    """Generates a random string.

    Args:
        max_chars: The maximum characters the string should have.

    Returns:
        Nothing.
    """
    return "".join([random.choice(string.ascii_letters) for _ in range(max_chars)])


def test_entry_attributes() -> None:
    """Test entry attributes.

    Failure:
        The entry name != "Test"
        The entry locations != given
        The entry dictionary != entry_map
        The entry json != json_map

    Returns:
        Nothing.
    """
    entry: Entry = Entry("Test", ["{HOME}", "johndoe"], ["etc"])
    json_string: str = '{"name": "Test", "locations": [["{HOME}", "johndoe"], ["etc"]]}'
    entry_map: Dict[str, Union[str, List[List[str]]]] = {
        "name": "Test",
        "locations": [["{HOME}", "johndoe"], ["etc"]],
    }
    assert entry.name == "Test"
    assert entry.locations == [
        Path(os.path.join(os.path.sep, str(Path().home()), "johndoe")),
        Path(os.path.join(os.path.sep, "etc")),
    ]
    assert entry.to_dict == entry_map
    assert entry.to_json == json_string


def test_entry_equality() -> None:
    """Test entry equality

    Failure:
        If entry != the other equal entry
        If entry == the other inequal entry

    Returns:
        Nothing.
    """
    entry: Entry = Entry("Test", ["{HOME}", "johndoe"], ["etc"])
    other_equal_entry: Entry = Entry("Test", ["{HOME}", "johndoe"], ["etc"])
    other_inequal_entry: Entry = Entry("NotEqual", ["etc", "lib"])
    assert entry == other_equal_entry
    assert entry != other_inequal_entry


def test_entry_locations_exists() -> None:
    """Test Entry.locations_exists()

    Failures:
        If the pathlib location exists value != the exists value generated by the method.

    Returns:
        Nothing.
    """
    existing: str = generate_random_string()
    non_existing: str = generate_random_string()
    os.mknod(existing)
    entry: Entry = Entry("Test", ["{HOME}", existing], ["{HOME}", non_existing])
    for location, exists in entry.locations_exists().items():  # type: ignore
        assert location.exists() == exists

    os.remove(existing)


def test_database_attributes_and_context_manager_and_database_creation_and_deletion() -> None:
    """Test database attributes, context manager, and database creation and deletion.

    Failure:
        If the database location != generated location
        If the database location doesn't exist
        If the database location != database.exists
        If there's nothing in database.entries
        If the entry name is != grub or zsh
        If the location exists even after context manager exit

    Returns:
        Nothing.
    """
    location: Path = Path().home() / generate_random_string()
    with Database(location) as database:
        assert database.location == location
        assert database.location.exists()
        assert database.exists() == database.location.exists()
        assert database.entries
        for entry in database.entries:
            assert entry.name == "grub" or entry.name == "zsh"

    assert not location.exists()


def test_add_entry_to_database() -> None:
    """Test adding entries to the database.

    Failure:
        If the added entry via method isn't in the database entries
        If the added entry via += isn't in the database entries
        If database doesn't raise an EntryExistsError even after trying to add an existing entry

    Returns:
        Nothing.
    """
    entry: Entry = Entry("Test", ["{HOME}", "johndoe"], ["etc"])
    entry_: Entry = Entry("OtherTest", ["{HOME}", "bob"], ["lib"])
    location: Path = Path().home() / generate_random_string()
    with Database(location) as database:
        database.add(entry)
        assert entry in database.entries
        database += entry_
        assert entry_ in database.entries
        with pytest.raises(exceptions.EntryExistsError):
            database.add(entry)


def test_remove_entry_from_database() -> None:
    """Test removing entries from the database.

    Failure:
        If the removed entry via method is still in the database entries
        If the removed entry via -= is still in the database entries
        If database doesn't raise an EntryNotFoundError even after trying to remove a non-existing entry

    Returns:
        Nothing.
    """
    location: Path = Path().home() / generate_random_string()
    entry: Entry = Entry("Test", ["{HOME}", "johndoe"], ["etc"])
    with Database(location) as database:
        database += entry
        database.remove(entry)
        assert entry not in database.entries
        database += entry
        database -= entry
        assert entry not in database.entries
        with pytest.raises(exceptions.EntryNotFoundError):
            database.remove(entry)
