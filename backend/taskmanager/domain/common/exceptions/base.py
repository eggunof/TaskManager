"""Defines base classes for exceptions"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class ApplicationError(Exception):
    """A base class for all application errors"""

    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        """Title of the error"""
        return "An application error occurred"


@dataclass(eq=False)
class DomainError(ApplicationError):
    """A base class for domain errors"""

    @property
    def title(self) -> str:
        return "A domain error occurred"
