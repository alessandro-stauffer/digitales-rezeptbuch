from recipe_input import ask_recipe
from recipe_management import add_recipe_id
from storage import load_recipes, save_recipes, import_recipe
from recipe_tools import scale_recipe, create_shopping_list


def create_recipe():
    recipes = load_recipes()
    recipe = ask_recipe()
    recipe = add_recipe_id(recipe, recipes)
    recipes.append(recipe)
    save_recipes(recipes)
    print(f"Rezept: {recipe['name']}")
    print(f"Portionen: {recipe['portions']}")
    print("Zutaten:")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient['amount']} {ingredient['unit']} {ingredient['name']}")
    print("Allergien:")
    for allergie in recipe["allergies"]:
        print(f"- {allergie}")


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


def show_menu():
    print("\n=== Digitales Rezeptbuch ===")
    print("1. Rezept erfassen")
    print("2. Rezept importieren")
    print("3. Rezepte anzeigen")
    print("4. Rezept bearbeiten")
    print("5. Rezept löschen")
    print("6. Zutatenmengen skalieren")
    print("7. Einkaufsliste erstellen")
    print("8. Nach Zutaten filtern")
    print("9. Favoriten")
    print("10. Allergien")
    print("0. Programm beenden")

def main():
    while True:
        show_menu()
        choice = input("Wähle eine Option: ")
        if choice == "0":
            break

        elif choice == "1":
            create_recipe()

        elif choice == "2":
            file_path = input("Dateipfad eingeben: ")
            import_new_recipe(file_path)

        elif choice == "3":
            recipes = load_recipes()
            for i, recipe in enumerate(recipes):
                print(i + 1, recipe["name"])

        elif choice == "4":
            pass

        elif choice == "5":
            pass

        elif choice == "6":
            recipes = load_recipes()

            for i, recipe in enumerate(recipes):
                print(i + 1, recipe["name"])

            number = input("Wähle eine Rezeptnummer: ")

            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(recipes):
                    selected_recipe = recipes[number - 1]
                    print(selected_recipe["name"])

                    new_portions = input("Für wie viele Personen?")
                    scaled_recipe = scale_recipe(selected_recipe, new_portions)

                    if scaled_recipe is not None:
                        print(scaled_recipe["name"], "für", scaled_recipe["portions"], "Personen")
                        for ingredient in scaled_recipe["ingredients"]:
                            print(ingredient["amount"], ingredient["unit"], ingredient["name"])
                else:
                    print("Diese Rezeptnummer existiert nicht.")
            else:
                print("Bitte eine gültige Zahl eingeben")

        elif choice == "7":
            recipes = load_recipes()

            for i, recipe in enumerate(recipes):
                print(i + 1, recipe["name"])

            number = input("Wähle eine Rezeptnummer: ")
            
            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(recipes):
                    selected_recipe = recipes[number - 1]
                    print(selected_recipe["name"])

                    new_portions = input("Für wie viele Personen? ")
                    shopping_list = create_shopping_list(selected_recipe, new_portions)

                    if shopping_list is not None:
                        for ingredient in shopping_list:
                            print(ingredient["amount"], ingredient["unit"], ingredient["name"])

                else:
                    print("Diese Rezeptnummer existiert nicht.")
            else:
                print("Bitte eine gültige Zahl eingeben.")


        elif choice == "8":
            pass

        elif choice == "9":
            pass

        elif choice == "10":
            pass

        else:
            print("Diese Option ist nicht verfügbar.")

if __name__ == "__main__":
    main()