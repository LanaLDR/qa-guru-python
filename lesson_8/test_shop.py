"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_full_quantity(self, product):
        assert product.check_quantity(product.quantity) == True

    def test_product_check_biggest_quantity(self, product):
        assert product.check_quantity(product.quantity+1) == False

    def test_product_buy(self, product):
        product.buy(999)
        assert product.quantity == 1

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product_in_cart(self, cart, product):
        cart.add_product(product)
        assert cart.products[product] == 1 and product in cart.products

    def test_sum_count_add_product_in_cart(self, cart, product):
        cart.add_product(product, 5)
        cart.add_product(product, 5)
        assert cart.products[product] == 10

    def test_remove_all_product_from_cart(self, cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product)
        assert len(cart.products) == 0

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        assert cart.products[product] == 1

    def test_remove_biggest_product_from_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 10)
        assert len(cart.products) == 0

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 9)
        cart.add_product(Product("pen", 250, "This is a pen", 999), 6)
        assert cart.get_total_price() == 2400

    def test_positive_buy_cart(self, cart, product):
        cart.add_product(product, 9)
        cart.buy()
        assert len(cart.products) == 0 and product.quantity == 991

    def test_negative_buy_cart(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()