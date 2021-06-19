

class Stock(object):

    def __init__(self, stock_name):
        self.name = stock_name
        self.products = {}

    def add(self, product):
        self.products[product.id] = product

    def remove(self, product):
        del self.products[product.id]

    def total_worth(self):
        products = self.products.values()
        return sum([prod.price for prod in products])

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"{self.name } - total products: {len(self)}"

