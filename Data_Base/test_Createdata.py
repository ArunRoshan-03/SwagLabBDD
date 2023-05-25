import pytest

from Data_Base.DatabaseConnection import DatabaseConnection
from utilise.BaseClass import BaseClass


class TestDatabaseConnection(BaseClass):
    # List of product names and prices
    # product_names = ['Product D', 'Product H', 'Product I']
    # product_prices = [10.99, 19.99, 7.99]

    @pytest.mark.ar
    def test_insert_data(self):
        db = DatabaseConnection(self.cursor)
        db.insert_data(self.product_names, self.product_prices, "swag")

    @pytest.mark.ar
    def test_retrieve_data(self):
        db = DatabaseConnection(self.cursor)
        db.retrieve_data("swag")
