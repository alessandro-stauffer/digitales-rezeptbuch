from navigation import clear_screen, choose_next_action
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


def scale_recipe_menu(selected_index=None):
    recipes = load_recipes()
    scaled_recipes = []

    while True:
        clear_screen()
        print("\n=== Rezepte skalieren ===\n")

        if selected_index is None:
            for i, recipe in enumerate(recipes):
                print(f"{i + 1}. {recipe['name']}")

            numbers = input("Wähle Rezeptnummer/n (z.B. 1,4): ")
        else:
            numbers = str(selected_index + 1)
            selected_index = None

        selected_numbers = numbers.split(",")

        previous_count = len(scaled_recipes)

        for number in selected_numbers:
            number = number.strip()

            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(recipes):
                    selected_recipe = recipes[number - 1]

                    new_portions = input(f"\nNeue Portionszahl für {selected_recipe['name']}: ")
                    scaled_recipe = scale_recipe(selected_recipe, new_portions)

                    if scaled_recipe is not None:
                        scaled_recipes.append(scaled_recipe)

                        print(f"\n=== {scaled_recipe['name']} ({scaled_recipe['portions']} Portionen) ===")

                        for ingredient in scaled_recipe["ingredients"]:
                            print(f"- {ingredient['name']}: {ingredient['amount']:g} {ingredient['unit']}")
                else:
                    print(f"Fehler: Rezeptnummer {number} existiert nicht.")
            else:
                print(f"Fehler: '{number}' ist keine gültige Rezeptnummer.")

        if len(scaled_recipes) == previous_count:
            print("Es wurden keine weiteren Rezepte skaliert.")

            choice = choose_next_action({
                "1": "Erneut versuchen",
                "2": "Zurück zum Hauptmenü"
            })

            if choice == "2":
                clear_screen()
                return

            continue

        choice = choose_next_action({
            "1": "Gemeinsame Einkaufsliste als PDF erstellen",
            "2": "Weiteres Rezept skalieren",
            "3": "Zurück zum Hauptmenü"
        })

        if choice == "1":
            clear_screen()
            shopping_list_menu(scaled_recipes)
            return

        if choice == "3":
            clear_screen()
            return

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
    print("\n--- Die Datei einkaufsliste.pdf wurde erstellt ---\n")


def shopping_list_menu(scaled_recipes=None):
    while True:
        if scaled_recipes is None:
            clear_screen()

        all_ingredients = []

        if scaled_recipes is not None:
            for recipe in scaled_recipes:
                for ingredient in recipe["ingredients"]:
                    all_ingredients.append(ingredient)

        else:   
            recipes = load_recipes()

            print("\n=== Einkaufsliste erstellen ===\n")

            for i, recipe in enumerate(recipes):
                print(f"{i + 1}. {recipe['name']}")

            numbers = input("Wähle Rezeptnummer/n (z.B. 1,2): ")
            selected_numbers = numbers.split(",")

            for number in selected_numbers:
                number = number.strip()

                if number.isdigit():
                    number = int(number)

                    if 1 <= number <= len(recipes):
                        selected_recipe = recipes[number - 1]

                        new_portions = input(f"\nNeue Portionszahl für {selected_recipe['name']}: ")
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

            choice = choose_next_action({
                "1": "Erneut versuchen",
                "2": "Zurück zum Hauptmenü"
            })

            if choice == "2":
                clear_screen()
                return

            scaled_recipes = None
            continue

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

        clear_screen()
        print("\n=== Gemeinsame Einkaufsliste ===")

        for ingredient in combined_ingredients:
            print(f"- {ingredient['name']}: {ingredient['amount']:g} {ingredient['unit']}")

        create_shopping_list_pdf(combined_ingredients)

        choice = choose_next_action({
            "1": "Weitere Einkaufsliste erstellen",
            "2": "Zurück zum Hauptmenü"
        })

        if choice == "1":
            scaled_recipes = None

        if choice == "2":
            clear_screen()
            return