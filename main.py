from recipe_input import ask_recipe
from recipe_management import add_recipe_id


recipes = []
recipe = ask_recipe()
recipe = add_recipe_id(recipe, recipes)
recipes.append(recipe)
print(recipes)

