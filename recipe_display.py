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
    print('\n === Deine Rezepte ===')

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


