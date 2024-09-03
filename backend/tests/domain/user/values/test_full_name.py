"""Tests for FullName value object"""

import pytest
from faker import Faker

from taskmanager.domain.user.exceptions import EmptyNameError, TooLongNameError
from taskmanager.domain.user.values import FullName
from taskmanager.domain.user.values.full_name import MAX_NAME_LENGTH


def test_create_full_name_with_middle_name_success(
    faker: Faker,
) -> None:
    """Test creating a full name with middle name"""
    first_name = faker.first_name()
    last_name = faker.last_name()
    middle_name = faker.first_name()
    full_name = FullName(first_name, last_name, middle_name)

    assert full_name.first_name == first_name
    assert full_name.last_name == last_name
    assert full_name.middle_name == middle_name

    assert str(full_name) == f"{first_name} {middle_name} {last_name}"


def test_create_full_name_without_middle_name_success(
    faker: Faker,
) -> None:
    """Test creating a full name without middle name"""
    first_name = faker.first_name()
    last_name = faker.last_name()
    full_name = FullName(first_name, last_name)

    assert full_name.first_name == first_name
    assert full_name.last_name == last_name
    assert full_name.middle_name is None

    assert str(full_name) == f"{first_name} {last_name}"


def test_create_full_name_empty_first_name(
    faker: Faker,
) -> None:
    """Test creating a full name with an empty first name, which should raise an EmptyNameError"""
    first_name = ""
    last_name = faker.last_name()

    with pytest.raises(EmptyNameError):
        FullName(first_name, last_name)


def test_create_full_name_too_long_first_name(
    faker: Faker,
) -> None:
    """Test creating a full name with a too long first name, which should raise a TooLongNameError"""
    first_name = faker.pystr(min_chars=MAX_NAME_LENGTH + 1, max_chars=MAX_NAME_LENGTH + 10)
    last_name = faker.last_name()

    with pytest.raises(TooLongNameError):
        FullName(first_name, last_name)


def test_create_full_name_empty_last_name(
    faker: Faker,
) -> None:
    """Test creating a full name with an empty last name, which should raise an EmptyNameError"""
    first_name = faker.first_name()
    last_name = ""

    with pytest.raises(EmptyNameError):
        FullName(first_name, last_name)


def test_create_full_name_too_long_last_name(
    faker: Faker,
) -> None:
    """Test creating a full name with a too long last name, which should raise a TooLongNameError"""
    first_name = faker.first_name()
    last_name = faker.pystr(min_chars=MAX_NAME_LENGTH + 1, max_chars=MAX_NAME_LENGTH + 10)

    with pytest.raises(TooLongNameError):
        FullName(first_name, last_name)


def test_create_full_name_empty_middle_name(
    faker: Faker,
) -> None:
    """Test creating a full name with an empty middle name, which should raise an EmptyNameError"""
    first_name = faker.first_name()
    last_name = faker.last_name()
    middle_name = ""

    with pytest.raises(EmptyNameError):
        FullName(first_name, last_name, middle_name)


def test_create_full_name_too_long_middle_name(
    faker: Faker,
) -> None:
    """Test creating a full name with a too long middle name, which should raise a TooLongNameError"""
    first_name = faker.first_name()
    last_name = faker.last_name()
    middle_name = faker.pystr(min_chars=MAX_NAME_LENGTH + 1, max_chars=MAX_NAME_LENGTH + 10)

    with pytest.raises(TooLongNameError):
        FullName(first_name, last_name, middle_name)
