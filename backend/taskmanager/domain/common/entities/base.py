"""Defines the base class for entities"""

from abc import ABC
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Entity(ABC):
    """A base class for entities"""

    id: UUID = field(default_factory=uuid4, init=False, kw_only=True)
