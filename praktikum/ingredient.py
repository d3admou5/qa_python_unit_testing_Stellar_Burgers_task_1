class Ingredient:
    """
    Модель ингредиента.
    Ингредиент: начинка или соус.
    У ингредиента есть тип (начинка или соус), название и цена.
    """

    def __init__(self, ingredient_type: str, name: str, price: float):
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type
