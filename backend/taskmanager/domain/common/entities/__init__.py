"""This module contains base classes and interfaces for domain models"""

from .aggregate_root import AggregateRoot
from .base import Entity

__all__ = (
    "Entity",
    "AggregateRoot",
)
