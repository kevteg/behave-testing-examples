from random import randint
from . import MIN_ID, MAX_ID, DEFAULT_TAX, HUNDRED_PER
from .exceptions import WrongTaxField 


class Product(object):

    def __init__(self, name, base_price, tax=DEFAULT_TAX):
        self.id = randint(MIN_ID, MAX_ID)
        self.name = name
        self.tax = tax
        self.base_price = base_price
        self.price = base_price

    @property
    def name(self):
        return self._name

    @property
    def tax(self):
        return self._tax

    @property
    def price(self):
        return self._price

    @name.setter
    def name(self, name):
        self._name = name.title()

    @price.setter
    def price(self, price):
        price = price + price*(self.tax/HUNDRED_PER)
        self._price = price

    @tax.setter
    def tax(self, tax):
        if tax < 0 or tax > HUNDRED_PER:
            raise WrongTaxField()

        self._tax = tax

    def __repr__(self):
        return f"Product('{self.name}', {self.base_price}, {self.tax})"

    def __str__(self):
        return f"{self.name}"
