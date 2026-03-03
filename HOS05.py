"""Main application logic for the contact book."""

from contact_book import (
    add_contact,
    remove_contact,
    search_contact,
    list_contacts,
)
from display import display_message, display_contact


def main() -> None:
    """Demonstrate basic operations of the contact book.

    A local dictionary is initialized so tests don't rely on the
    module-level global state in ``contact_book``.  Each helper is
    called with the ``store`` keyword argument.
    """
    display_message("Starting contact book demo")

    # initialize a fresh dictionary for testing
    test_contacts: dict = {}

    # add some entries
    add_contact("Alice", "555-1234", store=test_contacts)
    add_contact("Bob", "555-5678", store=test_contacts)

    # list all contacts
    contacts = list_contacts(store=test_contacts)
    display_message("All contacts:")
    for name, phone in contacts.items():
        display_contact(name, phone)

    # search for one
    phone = search_contact("Alice", store=test_contacts)
    if phone:
        display_message("Found Alice:")
        display_contact("Alice", phone)
    else:
        display_message("Alice not found")

    # remove Bob
    remove_contact("Bob", store=test_contacts)
    display_message("After removing Bob:")
    for name, phone in list_contacts(store=test_contacts).items():
        display_contact(name, phone)


if __name__ == "__main__":
    main()
