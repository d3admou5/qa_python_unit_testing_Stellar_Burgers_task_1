import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_assigns_bun(self):
        """Проверяем, что set_buns корректно устанавливает булочку"""
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_appends_to_list(self):
        """Проверяем, что add_ingredient добавляет ингредиент в список"""
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient_removes_from_list(self):
        """Проверяем, что remove_ingredient удаляет ингредиент по индексу"""
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert ingredient1 not in burger.ingredients
        assert ingredient2 in burger.ingredients

    def test_move_ingredient_changes_order(self):
        """Проверяем, что move_ingredient меняет порядок ингредиентов"""
        burger = Burger()
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)  # перемещаем первый в конец

        assert burger.ingredients == [ing2, ing3, ing1]

    @pytest.mark.parametrize("bun_price, ing_prices, expected", [
        (100, [50, 50], 300),   # 2*100 + 50 + 50 = 300
        (200, [], 400),         # 2*200 = 400
        (150, [100], 400),      # 2*150 + 100 = 400
    ])
    def test_get_price(self, bun_price, ing_prices, expected):
        """Проверяем, что get_price возвращает корректную цену"""
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ing_prices:
            ing = Mock()
            ing.get_price.return_value = price
            burger.add_ingredient(ing)

        assert burger.get_price() == expected

    def test_get_receipt_contains_bun_and_ingredients(self):
        """Проверяем, что get_receipt возвращает чек с булочкой и ингредиентами"""
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "Test Bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "Ketchup"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert "(==== Test Bun ====)" in receipt
        assert "= sauce Ketchup =" in receipt
        assert f"Price: {burger.get_price()}" in receipt
