import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

# Тест на корректное создание объекта Ingredient
    def test_create_ingredient(self):

        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100

# Тестируем метод get_name
    @pytest.mark.parametrize("name", ["cutlet", "sausage", "dinosaur"])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 150)

        assert ingredient.get_name() == name

# Тестируем метод get_type
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "test ingredient", 200)

        assert ingredient.get_type() == ingredient_type

# Тестируем метод get_price
    @pytest.mark.parametrize("price", [50, 100, 300.75])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "test ingredient", price)

        assert ingredient.get_price() == price
