"""Value object representing user's ID"""

from dataclasses import dataclass
from uuid import UUID

from taskmanager.domain.common.values import ValueObject


@dataclass(frozen=True)
class UserId(ValueObject[UUID]):
    """Class representing user ID"""
