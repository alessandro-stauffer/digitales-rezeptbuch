import json


def save_recipes(recipes):
    with open("data/recipes.json", "w", encoding="utf-8") as file:
        json.dump(recipes, file, ensure_ascii=False, indent=4)


def load_recipes():
    try:
        with open("data/recipes.json", "r", encoding="utf-8") as file:
            recipes = json.load(file)
    except FileNotFoundError:
        recipes = []
    except json.JSONDecodeError:
        print("Fehler: Die Rezeptdatei enthält ungültiges JSON.")
        raise

    return recipes