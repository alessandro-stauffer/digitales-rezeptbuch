from setup_dependencies import install_dependencies
install_dependencies()

from recipe_input import create_recipe_menu, import_recipe_menu
from storage import load_recipes
from recipe_tools import scale_recipe_menu, shopping_list_menu
from recipe_display import show_recipes_menu
from recipe_edit import edit_recipe_menu
from recipe_delete import delete_recipe_menu
from recipe_features import ingredient_filter, get_favorites, edit_favorites, allergies_filter
from terminal_tools import clear_screen, handle_menu_return

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
        clear_screen()
        show_menu()
        choice = input("Wähle eine Option: ")
        if choice == "0":
            break

        clear_screen()

        if choice == "1":
            create_recipe_menu()

        elif choice == "2":
            import_recipe_menu()

        elif choice == "3":
            show_recipes_menu()

        elif choice == "4":
            edit_recipe_menu()

        elif choice == "5":
            delete_recipe_menu()

        elif choice == "6":
            scale_recipe_menu()

        elif choice == "7":
            shopping_list_menu()

        elif choice == "8":
            ingredient_filter()

        elif choice == "9":
            get_favorites()

        elif choice == "10":
            allergies_filter()

        else:
            print("Diese Option ist nicht verfügbar.")
            
        handle_menu_return(choice)

if __name__ == "__main__":
    main()