"""This module contains custom exception classes for handling errors with username"""

from dataclasses import dataclass

from taskmanager.domain.common.exceptions import DomainError


@dataclass(eq=False)
class WrongUsernameValueError(ValueError, DomainError):
    """Exception for handling wrong usernames value errors"""

    username: str


class EmptyUsernameError(WrongUsernameValueError):
    """Exception for handling empty usernames errors"""

    @property
    def title(self) -> str:
        return "Username can't be empty"


class TooLongUsernameError(WrongUsernameValueError):
    """Exception for handling too long usernames errors"""

    @property
    def title(self) -> str:
        return f'Too long username "{self.username}"'
