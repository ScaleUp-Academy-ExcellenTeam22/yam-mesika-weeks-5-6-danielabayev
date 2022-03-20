def get_recipe_price(prices, optionals=[], **ingredients):
    total_price = 0
    for ingredient in ingredients:
        ingredient_amount = int(ingredients[ingredient]) / 100
        if ingredient in optionals:
            continue
        ingredient_price = ingredient_amount * prices[ingredient]
        total_price = total_price + ingredient_price
    print(total_price)


get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
get_recipe_price({})
