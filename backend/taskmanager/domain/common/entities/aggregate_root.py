"""Defines the base class for aggregated root"""

from abc import ABC
from dataclasses import dataclass

from .base import Entity, EntityId


@dataclass
class AggregateRoot(Entity[EntityId], ABC):
    """A class representing an aggregate root"""
