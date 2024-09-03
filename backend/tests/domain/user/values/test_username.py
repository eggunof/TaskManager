"""Tests for FullName value object"""

import pytest
from faker import Faker

from taskmanager.domain.user.exceptions import EmptyUsernameError, TooLongUsernameError
from taskmanager.domain.user.values import Username
from taskmanager.domain.user.values.username import MAX_USERNAME_LENGTH


def test_create_username_success(
    faker: Faker,
) -> None:
    """Test creating username"""
    name = faker.user_name()
    username = Username(name)
    assert username.to_raw() == name


def test_create_username_empty_name() -> None:
    """Test creating username with an empty name, which should raise an EmptyUsernameError"""
    name = ""

    with pytest.raises(EmptyUsernameError):
        Username(name)


def test_create_username_too_long_name(
    faker: Faker,
) -> None:
    """Test creating username with a too long name, which should raise a TooLongUsernameError"""
    name = faker.pystr(min_chars=MAX_USERNAME_LENGTH + 1, max_chars=MAX_USERNAME_LENGTH + 10)

    with pytest.raises(TooLongUsernameError):
        Username(name)
