"""Simple contact book module."""

contacts = {}


def add_contact(name: str, phone: str, store: dict | None = None) -> dict:
    """Add a contact to the contacts dictionary.

    If a specific dictionary is provided via ``store`` it will be used
    instead of the module-level ``contacts``.

    Args:
        name: The contact's name, used as the key.
        phone: The contact's phone number, used as the value.
        store: Optional dict to operate on.

    Returns:
        The updated contacts dictionary.
    """
    if store is None:
        store = contacts
    store[name] = phone
    return store


def remove_contact(name: str, store: dict | None = None) -> dict:
    """Remove a contact by name from the contacts dictionary.

    Operates on ``store`` if given, otherwise the module-level
    ``contacts``. Missing names are ignored.

    Args:
        name: The contact's name to remove.
        store: Optional dict to operate on.

    Returns:
        The updated contacts dictionary.
    """
    if store is None:
        store = contacts
    store.pop(name, None)
    return store


def search_contact(name: str, store: dict | None = None) -> str | None:
    """Retrieve the phone number for a given contact name.

    Args:
        name: The contact's name to look up.
        store: Optional dict to operate on.

    Returns:
        The phone number if found, otherwise None.
    """
    if store is None:
        store = contacts
    return store.get(name)


def list_contacts(store: dict | None = None) -> dict:
    """Return a copy of all contacts from provided dict or global.

    Args:
        store: Optional dict to list.

    Returns:
        A shallow copy of the contacts.
    """
    if store is None:
        store = contacts
    return store.copy()
