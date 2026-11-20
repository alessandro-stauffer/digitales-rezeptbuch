# Tool: Rezepte laden
from storage import load_recipes

# Test Funktion select_recipe
from recipe_tools import select_recipe

# Funktion Rezepte anzeigen
def show_recipes():

    # Schleife für R am Schluss
    while True:

        # Aktivierung Funktion Rezeptauswahl
        DetailsOfRecipe = select_recipe()

        # Absicherung Absturz wegen Schleife bei leerem Rezeptbuch
        if not DetailsOfRecipe:
            return

        # Detailansicht
        print('\n=== Rezeptdetails ===')

        print(f'Rezept: {DetailsOfRecipe['name']}')
        print(f'Portionen: {DetailsOfRecipe['portions']}')

        print("\nZutaten:")

        # Schleife geht alle Einzelheiten des Rezepts durch
        for ingredients in DetailsOfRecipe['ingredients']:
            print(f' - {ingredients['name']}: {ingredients['amount']:.0f} {ingredients['unit']}')
                        
        if DetailsOfRecipe['allergies'] == []:
            print('\nAllergien: keine erfasst')
        else: print(f'\nAllergien: {DetailsOfRecipe['allergies']}')
                        
        if DetailsOfRecipe['favorite'] == False:
            print('Favorit: nein\n')
        else: print('Favorit: ja\n')
                    
        print('=== VIEL FREUDE BEIM KOCHEN ! ===\n')

        # Schleife für weiterfahren Menüauswahl r oder h
        while True:
            move = input('wähle "R" für Rezeptliste oder "H" für Hauptmenü: ').strip().lower()

            # Schleife nach ungültiger Eingabe
            while move != "r" and move != "h":
                move = input('\n[ERROR] Eingabe ungültig ! (gib "r" oder "h" ein): ').lower().strip()

            if move == "r":
                break
            elif move == "h":
                return