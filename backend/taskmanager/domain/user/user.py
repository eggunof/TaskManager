"""User aggregate"""

from dataclasses import dataclass

from typing_extensions import Self

from taskmanager.domain.common.entities.aggregate_root import AggregateRoot
from taskmanager.domain.user.values import FullName, UserId, Username


@dataclass
class User(AggregateRoot[UserId]):
    """Class representing a user"""

    username: Username
    full_name: FullName

    @classmethod
    def create(
        cls,
        user_id: UserId,
        username: Username,
        full_name: FullName,
    ) -> Self:
        """Factory for creating a user"""
        user = cls(user_id, username, full_name)
        return user
