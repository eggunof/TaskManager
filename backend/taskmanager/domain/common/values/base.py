"""Defines the base class for value objects"""

from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

V = TypeVar("V", bound=Any)


@dataclass(frozen=True)
class ValueObject(Generic[V], ABC):
    """A base class for objects that represent values"""

    _value: V

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None: ...

    def to_raw(self) -> V:
        """Returns raw value"""
        return self._value
