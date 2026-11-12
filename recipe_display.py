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
        id = input('\nWähle Rezept-Nr.: ')

print('\nWähle Rezept-Nr.: ')

