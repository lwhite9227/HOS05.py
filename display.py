"""Utility module for displaying messages and contacts."""


def display_message(message: str) -> None:
    """Print a generic message to stdout."""
    print(message)


def display_contact(name: str, phone: str) -> None:
    """Print a formatted contact entry."""
    print(f"Name: {name}, Phone: {phone}")
