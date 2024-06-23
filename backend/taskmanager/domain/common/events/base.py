"""Defines the base class for events"""

from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar
from uuid import UUID, uuid4


@dataclass
class Event(ABC):
    """A base class for events"""

    title: ClassVar[str]

    id: UUID = field(default_factory=uuid4, init=False, kw_only=True)
    timestamp: datetime = field(
        default_factory=datetime.utcnow,
        init=False,
        kw_only=True,
    )
