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


def test_repr(some_item):
    assert some_item.__repr__() == "Item('Фен', 3000, 10)"


def test_str(some_item):
    assert some_item.__str__() == 'Фен'


def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 30000


def test_apply_discount(some_item):
    assert some_item.apply_discount() is None


def test_item_name():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("СуперСмартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item2.name == "СуперСмартфон"
    assert print(item2.name) == print("Наименования товара должно быть не больше 10 симвовов")


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5

    item1 = items[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1


def test_string_to_number():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
