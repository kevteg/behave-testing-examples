import pytest
from ..product import Product
from ..product.exceptions import WrongTaxField


@pytest.mark.parametrize("tax", [15, 20])
def test_basic_fields(tax):
    '''
    Creates a new product and validates the name is title case
    and the new price is the expected
    '''
    product_name = "the product title"
    base_price = 100
    new_product = Product(product_name, base_price, tax)
    assert new_product.name == product_name.title()
    assert new_product.price == base_price + base_price*(tax/100)


@pytest.mark.parametrize("n_tax", [-15, 200, 56])
def test_tax_value(n_tax):
    '''
    Check the tax value is expected
    '''
    try:
        product_name = "the product title"
        base_price = 100
        new_product = Product(product_name, base_price, n_tax)
        assert False
    except WrongTaxField:
        assert True
    except:
        assert False
