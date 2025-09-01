import praktikum.ingredient_types as ingr_types
from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    """ Тест на установку и смену булки """
    def test_set_buns_and_change(self):
        burger = Burger()
        bun1 = Bun('White bun', 100.0)
        bun2 = Bun('Black bun', 200.0)

        burger.set_buns(bun1)
        assert burger.bun == bun1

        burger.set_buns(bun2)  # меняем булку
        assert burger.bun == bun2

    """ Тест на добавление ингредиента (mock) """
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Mock Filling'
        mock_ingredient.get_price.return_value = 50.0
        mock_ingredient.get_type.return_value = ingr_types.INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == 'Mock Filling'
        assert burger.ingredients[0].get_price() == 50.0
        assert burger.ingredients[0].get_type() == ingr_types.INGREDIENT_TYPE_FILLING

    """ Тест на удаление ингредиента """
    def test_remove_ingredient(self):
        burger = Burger()
        mock1 = Mock()
        mock2 = Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)

        burger.remove_ingredient(0)

        # Должен остаться только второй
        assert burger.ingredients == [mock2]

    """ Тест на перемещение ингредиента """
    def test_move_ingredient(self):
        burger = Burger()
        mock1 = Mock()
        mock2 = Mock()
        mock3 = Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.add_ingredient(mock3)

        # Перемещаем 0-й (mock1) на позицию 2
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [mock2, mock3, mock1]

    """ Тест на подсчёт цены (динамически через Database) """
    def test_get_price(self):
        burger = Burger()
        db = Database()

        bun = db.available_buns()[0]  # black bun 100
        sauce = db.available_ingredients()[0]  # hot sauce 100
        filling = db.available_ingredients()[3]  # cutlet 100

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        # Ожидаемая цена: 2*цена булки + цена ингредиентов
        expected_price = bun.get_price() * 2 + sauce.get_price() + filling.get_price()

        assert burger.get_price() == expected_price

    """ Тест на формирование чека """
    def test_get_receipt(self):
        burger = Burger()
        db = Database()

        bun = db.available_buns()[0]  # black bun
        sauce = db.available_ingredients()[0]  # hot sauce
        filling = db.available_ingredients()[3]  # cutlet

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected_price = bun.get_price() * 2 + sauce.get_price() + filling.get_price()

        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {sauce.get_type().lower()} {sauce.get_name()} =\n"
            f"= {filling.get_type().lower()} {filling.get_name()} =\n"
            f"(==== {bun.get_name()} ====)\n\n"
            f"Price: {expected_price}"
        )

        assert burger.get_receipt() == expected_receipt
