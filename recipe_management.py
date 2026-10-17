def generate_next_id(recipes):
    highest_id = 0
    for recipe in recipes:
        if highest_id < recipe["id"]:
            highest_id = recipe["id"]
    next_id = highest_id + 1
    return next_id

def add_recipe_id(recipe, recipes):
    next_id = generate_next_id(recipes)
    recipe["id"] = next_id
    return recipe
