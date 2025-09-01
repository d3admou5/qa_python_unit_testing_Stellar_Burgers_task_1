import pytest
from praktikum.bun import Bun


class TestBun:

    def test_bun_returns_correct_name(self):
        # Проверяем, что get_name возвращает правильное название.
        bun = Bun("Флюоресцентная булка R2-D3", 988)
        assert bun.get_name() == "Флюоресцентная булка R2-D3"

    def test_bun_returns_correct_price(self):
        # Проверяем, что get_price возвращает правильную цену.
        bun = Bun("Флюоресцентная булка R2-D3", 988)
        assert bun.get_price() == 988

    @pytest.mark.parametrize(
        "name,price",
        [
            ("Флюоресцентная булка R2-D3", 988),
            ("Краторная булка N-200i", 1255),
        ]
    )
    def test_bun_with_different_data(self, name, price):
        # Проверяем оба вида булок.
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
