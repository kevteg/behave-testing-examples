from ..product import Product
import pytest


@pytest.fixture
def add_products_to_stock():
    def wrapper(stock, products):
        for p in range(int(products)):
            dummy_pr = Product(str(p), p)
            stock.add(dummy_pr)

    return wrapper
