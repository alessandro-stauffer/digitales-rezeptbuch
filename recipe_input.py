from validation import validate_portions, validate_text, validate_amount, validate_unit, validate_yes_no
from recipe_features import ask_recipe_allergies
from recipe_management import add_recipe_id
from storage import load_recipes, save_recipes, import_recipe
from navigation import clear_screen, choose_next_action

def ask_portions():
    portions = None
    while portions is None:
        portions = input("Anzahl Portionen eingeben: ")
        portions = validate_portions(portions)
        if portions is None:
            print("Ungültige Portionszahl. Bitte eine positive und ganze Zahl eingeben.")

    return portions

def ask_recipe_name():
    is_valid = False
    while not is_valid:
        recipe_name = input("Rezeptname eingeben: ")
        is_valid = validate_text(recipe_name)
        if not is_valid:
            print("Der Rezeptname darf nicht leer sein. Bitte gib einen Rezeptnamen ein.")

    return recipe_name

def ask_ingredient_name():
    is_valid = False
    while not is_valid:
        ingredient_name = input("Zutatenname eingeben: ")
        is_valid = validate_text(ingredient_name)
        if not is_valid:
            print("Der Zutatenname darf nicht leer sein. Bitte gib einen Zutatennamen ein.")

    return ingredient_name

def ask_ingredient_amount():
    ingredient_amount = None
    while ingredient_amount is None:
        ingredient_amount = input("Zutatenmenge eingeben: ")
        ingredient_amount = validate_amount(ingredient_amount)
        if ingredient_amount is None:
            print("Ungültige Mengenangabe. Bitte eine positive Ganzzahl oder eine positive Dezimalzahl eingeben.")

    return ingredient_amount

def ask_ingredient_unit():
    is_valid = False
    while not is_valid:
        ingredient_unit = input("Einheit eingeben (g, ml, Stück): ")
        is_valid = validate_unit(ingredient_unit)
        if not is_valid:
            print("Ungültige Mengeneinheit. Bitte eine gültige Mengeneinheit (g, ml oder Stück) eingeben.")

    return ingredient_unit

# Funktion zum Erfassen einer Zutat
def ask_ingredient():
    name = ask_ingredient_name()
    amount = ask_ingredient_amount()
    unit = ask_ingredient_unit()
    ingredient = {
        "name": name,
        "amount": amount,
        "unit": unit
    }

    return ingredient

#Funktion zum Erfassen mehrerer Zutaten
def ask_ingredients():
    ingredients = []
    more_ingredients = True
    while more_ingredients:
        ingredient = ask_ingredient()
        ingredients.append(ingredient)
        more_ingredients = None
        while more_ingredients is None:
            answer_text = input("Weitere Zutat hinzufügen (j/n): ")
            more_ingredients = validate_yes_no(answer_text)
            if more_ingredients is None:
                print("Ungültige Eingabe. Bitte mit j oder n antworten.")

    return ingredients

def ask_recipe():
    name = ask_recipe_name()
    portions = ask_portions()
    ingredients = ask_ingredients()
    clear_screen()
    print("=== Allergien auswählen ===\n")
    allergies = ask_recipe_allergies()
    recipe = {
        "name": name,
        "portions": portions,
        "ingredients": ingredients,
        "favorite": False,
        "allergies": allergies
    }
    return recipe

def create_recipe():
    while True:
        clear_screen()
        print("=== Neues Rezept erfassen ===\n")
        recipes = load_recipes()
        recipe = ask_recipe()
        clear_screen()
        recipe = add_recipe_id(recipe, recipes)
        recipes.append(recipe)
        save_recipes(recipes)
        print("=== Rezept erfolgreich erfasst ===\n ")
        print(f"Rezept: {recipe['name']}")
        print(f"Portionen: {recipe['portions']}")
        print("Zutaten:")
        for ingredient in recipe["ingredients"]:
            print(f"- {ingredient['amount']} {ingredient['unit']} {ingredient['name']}")
        print()
        print("Allergien:")
        for allergie in recipe["allergies"]:
            print(f"- {allergie}")

        while True:
            choice = choose_next_action({
                "1": "Weiteres Rezept erfassen",
                "2": "Erfasstes Rezept anzeigen",
                "3": "Erfasstes Rezept bearbeiten",
                "4": "Zurück zum Hauptmenü"
            })

            if choice == "1":
                break

            if choice == "2":
                from recipe_display import details_recipe
                clear_screen()
                details_recipe(recipe)

            if choice == "3":
                from recipe_edit import edit_recipe
                edit_recipe(len(recipes) - 1)
                return

            if choice == "4":
                clear_screen()
                return

def import_new_recipe():
    while True:
        clear_screen()
        file_path = input("Dateipfad eingeben: ")
        recipes = load_recipes()
        recipe = import_recipe(file_path)
        if recipe is not None:
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
            clear_screen()
            print(f"Rezept '{clean_recipe['name']}' erfolgreich importiert.")

        options = {
            "1": "Weiteres Rezept importieren",
            "2": "Zurück zum Hauptmenü"
        }

        if recipe is not None:
            options = {
                "1": "Weiteres Rezept importieren",
                "2": "Importiertes Rezept anzeigen",
                "3": "Zurück zum Hauptmenü"
            }

        while True:
            choice = choose_next_action(options)

            if choice == "1":
                break

            if choice == "2" and recipe is not None:
                from recipe_display import details_recipe
                clear_screen()
                details_recipe(clean_recipe)

                choice = choose_next_action({
                    "1": "Weiteres Rezept importieren",
                    "2": "Zurück zum Hauptmenü"
                })

                if choice == "1":
                    break

                clear_screen()
                return

            else:
                clear_screen()
                return