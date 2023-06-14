"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def some_item():
    return Item("Фен", 3000, 10)


def test_item_init(some_item):
    assert some_item.name == "Фен"
    assert some_item.price == 3000
    assert some_item.quantity == 10


def test_item_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 30000


def test_item_apply_discount(some_item):
    assert some_item.apply_discount() is None
