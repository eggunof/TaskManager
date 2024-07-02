"""Defines the base class for aggregate root"""

from abc import ABC
from dataclasses import dataclass, field

from taskmanager.domain.common.events import Event

from .base import Entity, EntityId


@dataclass
class AggregateRoot(Entity[EntityId], ABC):
    """A class representing an aggregate root"""

    _events: list[Event] = field(default_factory=list, init=False, repr=False, hash=False, compare=False)

    def register_event(self, event: Event) -> None:
        """Register an event for the aggregate"""
        self._events.append(event)

    def clear_events(self) -> None:
        """Clear all events for the aggregate"""
        self._events.clear()

    def get_events(self) -> list[Event]:
        """Get all events for the aggregate"""
        return self._events

    def pull_events(self) -> list[Event]:
        """Pull and clear all events for the aggregate"""
        events = self.get_events().copy()
        self.clear_events()
        return events
