import pytest
from nomadbrew.api import CoffeeShopAPI, CoffeeShop
from nomadbrew.data import CoffeeShopData


def test_mock_search():
    api = CoffeeShopAPI(api_key=None)
    shops = api.search("coffee shop", "Mock City")
    assert len(shops) == 1
    assert shops[0].name == "Mock Coffee Shop"


def test_data_layer():
    data = CoffeeShopData(data_file=":memory:")
    shop = CoffeeShop(name="Test Shop", address="123 Test St", wifi=True, outlets=True, vibe="Cozy")
    data.add(shop)
    shops = data.get_all()
    assert len(shops) == 1
    assert shops[0].name == "Test Shop"


def test_rate():
    data = CoffeeShopData(data_file=":memory:")
    shop = CoffeeShop(name="Test Shop", address="123 Test St", wifi=True, outlets=True, vibe="Cozy")
    data.add(shop)
    data.rate("Test Shop", 4.5)
    shops = data.get_all()
    assert shops[0].rating == 4.5