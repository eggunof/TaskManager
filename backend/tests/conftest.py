"""Global conftest file"""

import random

import pytest


@pytest.fixture(scope="session", autouse=True)
def faker_seed() -> int:
    """Pytest fixture for setting a random seed for Faker"""
    return random.randint(1, 100000)
