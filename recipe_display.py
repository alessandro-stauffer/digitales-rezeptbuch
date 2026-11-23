from terminal_tools import clear_screen
from recipe_edit import edit_recipe_menu
from recipe_delete import delete_recipe_menu
from recipe_tools import scale_recipe_menu

# Tool: Herstellung Verbindung json
import json

# Tool: Rezepte laden
from storage import load_recipes

# Funktion Rezepte anzeigen
def show_recipes():
    recipes = load_recipes()

    # Status Rezeptbuch ist leer
    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    # vorhandene Rezepte
    print('\n=== Deine Rezepte ===')

    # i = Startpunkt
    for i, recipe in enumerate (recipes):

         # +1 wegen Nummerierung ab 0
        print(i+1, recipe["name"])

    # Rezept öffnen
    number = input('\nWähle Rezept-Nr.: ')

    # Prüfung int
    if number.isdigit():

        # Umwandlung Zahl
        number = int(number)

        # Prüfung Rezeptliste Anz.
        if 1 <= number <= len(recipes):
            selected_recipe = recipes[number - 1]

            # Detailansicht
            print('\n --- Rezeptdetails --- ')
            print(f"Rezept: {selected_recipe['name']}")
            print(f"Portionen: {selected_recipe['portions']}")
            print("Zutaten")
            for ingredients in selected_recipe['ingredients']:
                print(f' - {ingredients['name']}: {ingredients['amount']} {ingredients['unit']}')
            print()

        # Fehleingaben
        else: print(' \n--- kein Rezept gefunden --- \n(Eingabe ungültig ! Siehe unter "Deine Rezepte" und gebe die Nummer des gewünschten Rezepts ein)\n') # falsche Zahl
    else: print ('\n--- kein Rezept gefunden ---\n(Eingabe ungültig ! Gib eine gültige Zahl ein)\n') # Buchstaben statt Zahl

# Loop ? main.py oder display.py ?
# Ansicht nochmals anpassen - aber zuerst gemeinsamer Test am Mo

def show_recipes_menu():
    show_recipes()

    while True:
        print("\n=== Was möchtest du als Nächstes tun? ===")
        print("1. Rezept bearbeiten")
        print("2. Rezept löschen")
        print("3. Rezept skalieren")
        print("4. Zurück zum Hauptmenü")

        choice = input("Wähle eine Option (1-4): ")

        if choice == "1":
            clear_screen()
            edit_recipe_menu()
            return

        elif choice == "2":
            clear_screen()
            delete_recipe_menu()
            return

        elif choice == "3":
            clear_screen()
            scale_recipe_menu()
            return

        elif choice == "4":
            return

        else:
            print("Ungültige Eingabe. Bitte wähle 1 bis 4.")
