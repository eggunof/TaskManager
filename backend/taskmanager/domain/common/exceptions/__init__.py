"""This module contains base classes and interfaces for domain-specific exceptions"""

from .base import AppError, DomainError

__all__ = (
    "AppError",
    "DomainError",
)
