import pytest
from praktikum.bun import Bun


class TestBun:

# Тест на корректное создание объекта Bun
    def test_create_bun(self):
        bun = Bun("black bun", 100)
        assert bun.name == "black bun"
        assert bun.price == 100

# Тестируем метод get_name с разными названиями
    @pytest.mark.parametrize("name", ["black bun", "white bun", "red bun"])
    def test_get_name(self, name):
        bun = Bun(name, 150)
        assert bun.get_name() == name

# Тестируем метод get_price с разными значениями цены
    @pytest.mark.parametrize("price", [50, 100, 250.5])
    def test_get_price(self, price):
        bun = Bun("test bun", price)
        assert bun.get_price() == price
