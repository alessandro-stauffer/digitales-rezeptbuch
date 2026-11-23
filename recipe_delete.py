# Tool: Herstellung Verbindung json
import json

# Tool: Rezepte laden
from storage import load_recipes

# Tool: Rezepte speichern
from storage import save_recipes

# Terminal zu leeren
from terminal_tools import clear_screen

def delete_recipe():
    recipes = load_recipes()

    # Status Rezeptbuch ist leer ()
    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    # vorhandene Rezepte ()
    print('\n=== Deine Rezepte ===')
    for i, recipe in enumerate (recipes):
        print(i+1, recipe["name"])

    # Rezept fürs Löschen wählen
    number = input('\nWähle Rezept-Nr. zum löschen: ')

# Prüfung int & Umwandlung Zahl ()
    if number.isdigit():
        number = int(number)

        # Prüfung Rezeptliste Anz. ()
        if 1 <= number <= len(recipes):
            selected_recipe = recipes[number - 1]   

            # Sicherheitsfrage
            decide = input(f'\n{selected_recipe['name']} wirklich löschen? (j/n): ')
            if decide.lower().strip() == "j":

                # löschen über Position Liste
                recipes.pop(number -1)
                save_recipes(recipes)
                print('\n--- Rezept erfolgreich gelöscht --- \n')
            else: print ('\n--- Löschvorgang abgebrochen --- \n')

        # Fehleingaben ()
        else: print ('\n--- kein Rezept gefunden --- \n(Eingabe ungültig ! Siehe unter "Deine Rezepte" und gebe die Nummer des gewünschten Rezepts ein)\n')
    else: print('\n--- kein Rezept gefunden ---\n(Eingabe ungültig ! Gib eine gültige Zahl ein)\n') 

# Anzeige nachträglich nochmal anpassen, aber zuerst gemeinsamer Funktionstest am Mo

def delete_recipe_menu():
    while True:
        delete_recipe()

        while True:
            print("\n=== Was möchtest du als Nächstes tun? ===")
            print("1. Weiteres Rezept löschen")
            print("2. Zurück zum Hauptmenü")

            choice = input("Wähle eine Option (1 oder 2): ")

            if choice == "1":
                clear_screen()
                break

            elif choice == "2":
                return

            else:
                print("Ungültige Eingabe. Bitte wähle 1 oder 2.")   