"""Value object representing username"""

from dataclasses import dataclass

from taskmanager.domain.common.values import ValueObject
from taskmanager.domain.user.exceptions import EmptyUsernameError, TooLongUsernameError

MAX_USERNAME_LENGTH = 32


@dataclass(frozen=True)
class Username(ValueObject[str]):
    """Class representing username"""

    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyUsernameError(self.value)
        if len(self.value) > MAX_USERNAME_LENGTH:
            raise TooLongUsernameError(self.value)
