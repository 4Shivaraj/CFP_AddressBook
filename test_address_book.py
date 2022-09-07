import pytest
from address_book import Contact, AddressBook
from book_log import get_logger

lg = get_logger("(pytest_log)", file_name="address_book_log.log")


@pytest.fixture
def contact_object():
    """
    :return: contact object
    """
    try:
        return Contact(1, "shivaraj", "gowda", "bangalore", 876559878, "4shivaraj.gowda@gmail.com")
    except Exception as e:
        lg.error(e)


@pytest.fixture
def address_book_object():
    """
    :return: address book object
    """
    try:
        return AddressBook("home")
    except Exception as e:
        lg.error(e)


def test_full_name(contact_object):
    """
    testing full name method
    :param contact_object: object of contat class
    :return: None
    """
    try:
        name = "shivaraj gowda"
        contact_object.full_name == name
        print(contact_object.full_name)
    except Exception as e:
        lg.error(e)


def test_add_contact(contact_object, address_book_object):
    """
    testing the add contact method with length function
    :param contact_object: object of contact class
    :param address_book_object: object of address book class
    :return: None
    """
    try:
        assert len(address_book_object) == 0  # len(address_book_object.contact_dict) used __len__ method
        address_book_object.add_contact(contact_object)
        assert len(address_book_object) == 1
        contact2 = Contact(2, "cheluvesh", "b", "vijayanagar", 965678656, "cheluveshab@gmaiil.com")
        address_book_object.add_contact(contact2)
        assert len(address_book_object) == 2
        print(len(address_book_object))
    except Exception as e:
        lg.error(e)


def test_get_contact(contact_object, address_book_object):
    """
    testing get contact function
    :param contact_object: object of contact class
    :param address_book_object: object of address book class
    :return: None
    """
    try:
        address_book_object.add_contact(contact_object)
        actual = address_book_object.get_contact("shivaraj")
        assert isinstance(actual, Contact)
        assert actual.first_name == "shivaraj"
        print(actual.first_name)
    except Exception as e:
        lg.error(e)


def test_update_contact(contact_object, address_book_object):
    """
        testing update contact function
        :param contact_object: object of contact class
        :param address_book_object: object of address book class
        :return: None
    """
    try:
        address_book_object.add_contact(contact_object)
        address_book_object.update_contact(1, "shivaraj", "k", "basaveshwarnagar", 9876545673, "4shivayash@gmail.com")
        assert contact_object.last_name == "k"
        print(contact_object.last_name)
        assert contact_object.email == "4shivayash@gmail.com"
        print(contact_object.email)
    except Exception as e:
        lg.error(e)


def test_delete_contact(contact_object, address_book_object):
    """
        testing delete contact function
        :param contact_object: object of contact class
        :param address_book_object: object of address book class
        :return: None
    """
    try:
        address_book_object.add_contact(contact_object)
        assert len(address_book_object) == 1
        address_book_object.delete_contact("shivaraj")
        assert len(address_book_object) == 0
        print(len(address_book_object))
    except Exception as e:
        lg.error(e)


"""
============================= test session starts =============================
collecting ... collected 5 items

test_address_book.py::test_full_name PASSED                              [ 20%]shivaraj gowda

test_address_book.py::test_add_contact PASSED                            [ 40%]2

test_address_book.py::test_get_contact PASSED                            [ 60%]shivaraj

test_address_book.py::test_update_contact PASSED                         [ 80%]k
4shivayash@gmail.com

test_address_book.py::test_delete_contact PASSED                         [100%]0


============================== 5 passed in 0.02s ==============================
"""
