from validation import validate_portions, validate_text, validate_amount, validate_unit, validate_yes_no
from recipe_features import ask_recipe_allergies

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
    allergies = ask_recipe_allergies()
    recipe = {
        "name": name,
        "portions": portions,
        "ingredients": ingredients,
        "favorite": False,
        "allergies": allergies
    }
    return recipe

