from recipe_input import create_recipe, import_new_recipe
from storage import load_recipes
from recipe_tools import scale_recipe_menu, shopping_list_menu
from recipe_display import show_recipes
from recipe_edit import edit_recipe
from recipe_delete import delete_recipe
from recipe_features import ingredient_filter, get_favorites, edit_favorites, allergies_filter

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
    print("10. Allergien filtern")
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
            import_new_recipe(input("Dateipfad eingeben: "))

        elif choice == "3":
            show_recipes()

        elif choice == "4":
            edit_recipe()

        elif choice == "5":
            delete_recipe()

        elif choice == "6":
            scale_recipe_menu()

        elif choice == "7":
            shopping_list_menu()

        elif choice == "8":
            ingredient_filter()

        elif choice == "9":
            edit_favorites()

        elif choice == "10":
            allergies_filter()

        else:
            print("Diese Option ist nicht verfügbar.")

if __name__ == "__main__":
    main()