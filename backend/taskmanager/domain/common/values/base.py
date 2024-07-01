"""Defines the base class for value objects"""

from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

V = TypeVar("V", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC):
    """A base class for objects that represent values"""

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        """Check the value is valid to create this value object."""


@dataclass(frozen=True)
class ValueObject(Generic[V], BaseValueObject, ABC):
    """A base class for objects that represent only one value"""

    value: V

    def to_raw(self) -> V:
        """Return a raw value"""
        return self.value
