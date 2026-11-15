import json
from validation import validate_import_recipe


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

# Funktion wurde aufgrund des Feedbacks von Dr. Härer
# während der Prüfung der User Stories erstellt.
def import_recipe(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            recipe = json.load(file)
        if not validate_import_recipe(recipe):
            print("Das Rezept enthält ungültige Daten.")
            return None
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
        return None
    except json.JSONDecodeError:
        print("Die Importdatei ist beschädigt.")
        return None

    return recipe