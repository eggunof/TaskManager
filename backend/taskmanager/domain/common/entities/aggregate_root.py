"""Defines the base class for aggregated root"""

from abc import ABC
from dataclasses import dataclass, field

from taskmanager.domain.common.entities.base import Entity
from taskmanager.domain.common.events.base import Event


@dataclass
class AggregateRoot(Entity, ABC):
    """A class representing an aggregate root"""

    _events: list[Event] = field(default_factory=list, init=False, repr=False, hash=False, compare=False)

    def register_event(self, event: Event) -> None:
        """Register an event for the aggregate root"""
        self._events.append(event)

    def clear_events(self) -> None:
        """Clear all events for the aggregate root"""
        self._events.clear()

    def get_events(self) -> list[Event]:
        """Get all events for the aggregate root"""
        return self._events

    def pull_events(self) -> list[Event]:
        """Pull and clear all events for the aggregate root"""
        events = self.get_events().copy()
        self.clear_events()
        return events
