from validation import validate_portions, validate_text, validate_amount, validate_unit, validate_yes_no


def ask_portions():
    portions = None
    while portions is None:
        portions = input("Wie viele Portionen möchtest du erfassen?")
        portions = validate_portions(portions)
        if portions is None:
            print("Ungültige Portionszahl. Bitte eine positive und ganze Zahl eingeben.")

    return portions

def ask_recipe_name():
    is_valid = False
    while not is_valid:
        recipe_name = input("Gib den gewünschten Namen deines Rezeptes ein:")
        is_valid = validate_text(recipe_name)
        if not is_valid:
            print("Der Rezeptname darf nicht leer sein. Bitte gib einen Rezeptnamen ein.")

    return recipe_name

def ask_ingredient_name():
    is_valid = False
    while not is_valid:
        ingredient_name = input("Gib den gewünschten Namen deiner Zutat ein:")
        is_valid = validate_text(ingredient_name)
        if not is_valid:
            print("Der Zutatenname darf nicht leer sein. Bitte gib einen Zutatennamen ein.")

    return ingredient_name

def ask_ingredient_amount():
    ingredient_amount = None
    while ingredient_amount is None:
        ingredient_amount = input("Welche Menge benötigst du? Bitte eine positive Zahl eingeben:")
        ingredient_amount = validate_amount(ingredient_amount)
        if ingredient_amount is None:
            print("Ungültige Mengenangabe. Bitte eine postive Ganzzahl oder eine positive Dezimalzahl eingeben.")

    return ingredient_amount

def ask_ingredient_unit():
    is_valid = False
    while not is_valid:
        ingredient_unit = input("Welche Mengeneinheit (g, ml oder Stück) möchtest du verwenden?")
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
            answer_text = input("Möchtest du eine weitere Zutat hinzufügen (j oder n)?")
            more_ingredients = validate_yes_no(answer_text)
            if more_ingredients is None:
                print("Ungültige Eingabe. Bitte mit j oder n antworten.")

    return ingredients