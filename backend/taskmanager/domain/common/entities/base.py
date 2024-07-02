"""Defines the base class for entities"""

from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from taskmanager.domain.common.values import ValueObject

EntityId = TypeVar("EntityId", bound=ValueObject[Any])


@dataclass
class Entity(Generic[EntityId], ABC):
    """A base class for entities"""

    id: EntityId

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.id == other.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
