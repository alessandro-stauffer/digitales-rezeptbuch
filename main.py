from recipe_input import ask_recipe
from recipe_management import add_recipe_id
from storage import load_recipes, save_recipes


def create_recipe():
    recipes = load_recipes()
    recipe = ask_recipe()
    recipe = add_recipe_id(recipe, recipes)
    recipes.append(recipe)
    save_recipes(recipes)
    print(recipes)