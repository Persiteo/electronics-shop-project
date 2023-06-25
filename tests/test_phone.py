import pytest

from src.phone import Phone


@pytest.fixture
def phone_apple():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str(phone_apple):
    assert str(phone_apple.name) == 'iPhone 14'


def test_repr(phone_apple):
    assert repr(phone_apple) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone_apple):
    assert phone_apple.number_of_sim == 2

