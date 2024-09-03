"""This module contains custom exception classes for handling errors with users' value objects"""

from .full_name import EmptyNameError, TooLongNameError, WrongNameValueError
from .username import EmptyUsernameError, TooLongUsernameError, WrongUsernameValueError

__all__ = (
    "WrongNameValueError",
    "EmptyNameError",
    "TooLongNameError",
    "WrongUsernameValueError",
    "EmptyUsernameError",
    "TooLongUsernameError",
)
