from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:

# Тест на получение доступных булочек.
    def test_get_available_buns(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        assert len(available_buns) == 3

# Тест на получение доступных ингридиентов.
    def test_get_available_ingredients(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == 6

# Тест на получение доступных соусов.
    def test_get_quantity_available_sauces(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_sauce = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(type_sauce) == 3

# Тест на получение доступных начинок.
    def test_get_quantity_available_fillings(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(type_fillings) == 3

# Тест на получение цен на ингридиенты.
    def test_get_available_ingredients_prices(self):
        data_price = Database()
        ingredients = data_price.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        assert price['hot sauce'] == 100
