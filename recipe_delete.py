# Tool: Rezepte laden
from storage import load_recipes

# Tool: Rezepte speichern
from storage import save_recipes

# Tool: Rezeptliste
from recipe_tools import select_recipe

def delete_recipe():

    # Schleife für R am Schluss
    while True:
        DelRecipe = select_recipe()

        # Absicherung Absturz wegen Schleife bei leerem Rezeptbuch
        if not DelRecipe:
            return

        # Schleife für Sicherheitsfrage
        while True:
            # Sicherheitsfrage
            decide = input(f'\n{DelRecipe['name']} wirklich löschen? (j/n): ')
            if decide.lower().strip() == "j":
                ListOfRecipes = load_recipes()

                # löschen über Position Liste
                ListOfRecipes.remove(DelRecipe)
                save_recipes(ListOfRecipes)
                print('\n--- Rezept erfolgreich gelöscht --- \n')
                break
                
            elif decide.strip().lower() == "n":
                print ('\n--- Löschvorgang abgebrochen --- \n')
                break
                            
            else: print('\n[ERROR] Eingabe ungültig ! (gib "J" oder "N" ein): ')

        # Schleife für weiterfahren Menüauswahl r oder h
        while True:
                move = input('Wähle "R" für Rezeptliste oder "H" für Hauptmenü: ').strip().lower()
                

                while move != "r" and move != "h":
                    move = input('\n[ERROR] Eingabe ungültig ! (gib "R" oder "H" ein): ').lower().strip()

                if move == "r":
                    break
            
                elif move == "h":
                    return
