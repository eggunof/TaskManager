"""Defines base classes for exceptions"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class AppError(Exception):
    """A base class for all errors"""

    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        """Title of the error"""
        return "An app error occurred"


@dataclass(eq=False)
class DomainError(AppError):
    """A base class for domain errors"""

    @property
    def title(self) -> str:
        return "A domain error occurred"
