from recipe_input import ask_recipe
from recipe_management import add_recipe_id
from storage import load_recipes, save_recipes, import_recipe


def create_recipe():
    recipes = load_recipes()
    recipe = ask_recipe()
    recipe = add_recipe_id(recipe, recipes)
    recipes.append(recipe)
    save_recipes(recipes)
    print(recipes)

def import_new_recipe(file_path):
    recipes = load_recipes()
    recipe = import_recipe(file_path)
    if recipe is None:
        return
    clean_recipe = {
        "name": recipe["name"],
        "portions": recipe["portions"],
        "ingredients": recipe["ingredients"]
    }
    clean_recipe = add_recipe_id(clean_recipe, recipes)
    clean_recipe["favorite"] = False
    clean_recipe["allergies"] = []
    recipes.append(clean_recipe)
    save_recipes(recipes)
