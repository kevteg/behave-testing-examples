from pytest_bdd import given, when, then, scenario, parsers
from ...utils.stock import Stock
from ...product import Product


@scenario(
    "../features/stock.feature",
    "Adding new products to the stock",
    example_converters=dict(products=int, extra_products=int, new_count=int)
)
def test_add_products():
    pass


@given("We have a stock with <products> products", target_fixture="stock")
def stock(products, add_products_to_stock):
    stock = Stock('The stock')
    add_products_to_stock(stock, products)
    return stock


@when("I add <extra_products> to the stock")
def add_stock(stock, extra_products, add_products_to_stock):
    add_products_to_stock(stock, extra_products)


@then("I should now have <new_count> products")
def new_stock_number(stock, new_count):
    assert len(stock) == new_count
