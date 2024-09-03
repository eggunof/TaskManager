"""This module contains custom exception classes for handling errors with fullname"""

from dataclasses import dataclass

from taskmanager.domain.common.exceptions import DomainError


@dataclass(eq=False)
class WrongNameValueError(ValueError, DomainError):
    """Exception for handling wrong name values errors"""

    name: str
    text: str

    @property
    def title(self) -> str:
        return self.text


class EmptyNameError(WrongNameValueError):
    """Exception for handling empty names errors"""


class TooLongNameError(WrongNameValueError):
    """Exception for handling too long names errors"""
