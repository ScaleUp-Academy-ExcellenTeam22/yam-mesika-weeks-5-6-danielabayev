def get_recipe_price(prices: map, optionals: list = [], **ingredients: map) -> int:
    """
    This function get the ingredients and their prices, the ingredients we dont need and the amount from every
    ingredient and return the price the cake will cost to us.
    :param prices: A dictionary of ingredients needed to make the cake.
    :param optionals: A list of ingredients that we will ignore in the price calculation.
    :param ingredients: The amount of ingredient (in grams) from which we want to buy for the cake.
    :return: The price we need to pay on all the ingredients.
    """
    total_price = 0
    for ingredient in ingredients:
        ingredient_amount = int(ingredients[ingredient]) / 100
        if ingredient in optionals:
            continue
        ingredient_price = ingredient_amount * prices[ingredient]
        total_price = total_price + ingredient_price
    print(total_price)


if __name__ == '__main__':
    get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
    get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
    get_recipe_price({})
