"""Defines the base class for entities"""

from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from taskmanager.domain.common.values.base import ValueObject

EntityId = TypeVar("EntityId", bound=ValueObject[Any])


@dataclass
class Entity(Generic[EntityId], ABC):
    """A base class for entities"""

    id: EntityId
