from recipe_tools import select_recipe
from recipe_tools import details_recipe

# Funktion REZEPTE ANZEIGEN
def show_recipes():

    # Schleife für R am Schluss
    while True:

        # Aktivierung Funktion Rezeptauswahl
        SelectRecipe = select_recipe()

        # Absicherung Absturz wegen Schleife bei leerem Rezeptbuch
        if not SelectRecipe:
            return

        details_recipe(SelectRecipe)
        print('\n=== VIEL FREUDE BEIM KOCHEN ! ===\n')
            
        # Schleife für weiterfahren Menüauswahl r oder h
        while True:
            move = input('wähle "R" für Rezeptliste oder "H" für Hauptmenü: ').strip().lower()

            # Schleife nach ungültiger Eingabe
            while move != "r" and move != "h":
                move = input('\n[ERROR] Eingabe ungültig ! (gib "R" oder "H" ein): ').lower().strip()

            if move == "r":
                break
            elif move == "h":
                return
