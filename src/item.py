import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception("Что-то не так")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]
            raise Exception('Длина наименования товара должна быть не больше 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        cls.all = []
        with open(os.path.join(os.path.dirname(__file__), 'items.csv'), newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for each_row in reader:
                name = each_row['name']
                price = each_row['price']
                quantity = each_row['quantity']
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(value):
        """
        Метод, возвращающий число из числа-строки
        """
        number = int(float(value))
        return number
