from validation import validate_portions

def scale_recipe(recipe, new_portions):
    new_portions = validate_portions(new_portions)
    if new_portions is None:
        print("Ungültige Portionszahl.")
        return None

    old_portions  = recipe["portions"]
    factor = new_portions / old_portions

    new_ingredients = []

    for ingredient in recipe["ingredients"]:
        new_amount = ingredient["amount"] * factor

        new_ingredient = {
            "name": ingredient["name"],
            "amount": new_amount,
            "unit": ingredient["unit"]
        }
        new_ingredients.append(new_ingredient)

    new_recipe = recipe.copy()
    new_recipe["portions"] = new_portions
    new_recipe["ingredients"] = new_ingredients

    return new_recipe