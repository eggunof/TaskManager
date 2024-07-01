"""Defines the base class for entities"""

from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Generic, TypeVar

from taskmanager.domain.common.events import Event
from taskmanager.domain.common.values import ValueObject

EntityId = TypeVar("EntityId", bound=ValueObject[Any])


@dataclass
class Entity(Generic[EntityId], ABC):
    """A base class for entities"""

    id: EntityId

    _events: list[Event] = field(default_factory=list, init=False, repr=False, hash=False, compare=False)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.id == other.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def register_event(self, event: Event) -> None:
        """Register an event for the entity"""
        self._events.append(event)

    def clear_events(self) -> None:
        """Clear all events for the entity"""
        self._events.clear()

    def get_events(self) -> list[Event]:
        """Get all events for the entity"""
        return self._events

    def pull_events(self) -> list[Event]:
        """Pull and clear all events for the entity"""
        events = self.get_events().copy()
        self.clear_events()
        return events
