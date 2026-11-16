from validation import validate_portions
from storage import load_recipes
from reportlab.pdfgen import canvas

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


def scale_recipe_menu():
    recipes = load_recipes()

    for i, recipe in enumerate(recipes):
        print(i + 1, recipe["name"])

    numbers = input("Wähle Rezeptnummer/n (z.B. 1,4): ")
    selected_numbers = numbers.split(",")

    scaled_recipes = []

    for number in selected_numbers:
        number = number.strip()

        if number.isdigit():
            number = int(number)

            if 1 <= number <= len(recipes):
                selected_recipe = recipes[number - 1]
                print(selected_recipe["name"])

                new_portions = input("Für wie viele Personen? ")
                scaled_recipe = scale_recipe(selected_recipe, new_portions)

                if scaled_recipe is not None:
                    scaled_recipes.append(scaled_recipe)

                    print(scaled_recipe["name"], "für", scaled_recipe["portions"], "Personen")

                    for ingredient in scaled_recipe["ingredients"]:
                        print(ingredient["amount"], ingredient["unit"], ingredient["name"])
            else:
                print(f"Fehler: Rezeptnummer {number} existiert nicht.")
        else:
            print(f"Fehler: '{number}' ist keine gültige Rezeptnummer.")

    if not scaled_recipes:
        print("Es wurden keine Rezepte skaliert.")
        return

    print("\n=== Was möchtest du als Nächstes tun? ===")
    print("1. Gemeinsame Einkaufsliste als PDF erstellen")
    print("2.  Zurück zum Hauptmenü")

    while True:
        answer = input("Wähle eine Option (1 oder 2): ")

        if answer == "1":
            shopping_list_menu(scaled_recipes)
            return

        elif answer == "2":
            return

        else:
            print("Ungültige Eingabe.")


def create_shopping_list(recipe, new_portions):
    scaled_recipe = scale_recipe(recipe, new_portions)
    if scaled_recipe is None:
        return None

    shopping_list = []

    for ingredient in scaled_recipe["ingredients"]:
        shopping_list.append(ingredient)

    return shopping_list


def create_shopping_list_pdf(ingredients):
    pdf = canvas.Canvas("einkaufsliste.pdf")

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 800, "Gemeinsame Einkaufsliste")

    pdf.setFont("Helvetica", 12)
    y = 760

    for ingredient in ingredients:
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 760
            
        text = f"{ingredient['amount']:g} {ingredient['unit']} {ingredient['name']}"
        pdf.drawString(50, y, text)
        y -= 25

    pdf.save()
    print("Die Datei einkaufsliste.pdf wurde erstellt")


def shopping_list_menu(scaled_recipes=None):
    all_ingredients = []

    if scaled_recipes is not None:
        for recipe in scaled_recipes:
            for ingredient in recipe["ingredients"]:
                all_ingredients.append(ingredient)

    else:   
        recipes = load_recipes()

        for i, recipe in enumerate(recipes):
            print(i + 1, recipe["name"])

        numbers = input("Wähle Rezeptnummer/n (z.B. 1,2): ")
        selected_numbers = numbers.split(",")

        for number in selected_numbers:
            number = number.strip()

            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(recipes):
                    selected_recipe = recipes[number - 1]
                    print(selected_recipe["name"])

                    new_portions = input ("Für wie viele Personen? ")
                    shopping_list =  create_shopping_list(selected_recipe, new_portions)

                    if shopping_list is not None:
                        for ingredient in shopping_list:
                            all_ingredients.append(ingredient)

                else:
                    print(f"Fehler: Rezeptnummer {number} existiert nicht.")

            else:
                print(f"Fehler: '{number}' ist keine gültige Rezeptnummer.")

    if not all_ingredients:
        print("Es konnten keine Zutaten für die Einkaufsliste gefunden werden.")
        return

    combined_ingredients = []

    for ingredient in all_ingredients:
        found = False

        for existing in combined_ingredients:
            if (ingredient["name"].lower() == existing["name"].lower() and ingredient["unit"] == existing["unit"]):
                existing["amount"] += ingredient["amount"]
                found = True
                break

        if not found:
            combined_ingredients.append(ingredient.copy())

    print("\n=== Gemeinsame Einkaufsliste ===")

    for ingredient in combined_ingredients:
        print(ingredient["amount"], ingredient["unit"], ingredient["name"])

    create_shopping_list_pdf(combined_ingredients)