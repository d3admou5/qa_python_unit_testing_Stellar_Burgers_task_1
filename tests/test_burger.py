import pytest
from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

# Тест на установку булочек с параметризацией.
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_set_bun(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == name
        assert burger.bun.get_price() == price

# Тест на добавление ингредиента с параметризацией.
    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200)
    ])
    def test_add_ingredient(self, ing_type, name, price):
        burger = Burger()
        ingredient = Ingredient(ing_type, name, price)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

# Тест на удаление ингредиента.
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

# Тест на получение цены бургера с реальными объектами.
    def test_get_price(self):
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])
        burger.add_ingredient(db.available_ingredients()[0])
        burger.add_ingredient(db.available_ingredients()[3])
        assert burger.get_price() == 400

# Тест на получение чека с реальными объектами.
    def test_get_receipt(self):
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[0])
        burger.add_ingredient(db.available_ingredients()[0])
        burger.add_ingredient(db.available_ingredients()[3])

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 400"
        )
        assert burger.get_receipt() == expected_receipt
