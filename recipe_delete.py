# Für Text und Terminal clear zu beahalten
from navigation import clear_screen, choose_next_action

# Tool: Rezepte laden
from storage import load_recipes

# Tool: Rezepte speichern
from storage import save_recipes

# Tool: Rezeptliste
from recipe_display import select_recipe, show_recipes

def delete_recipe():

    # Schleife für R am Schluss
    while True:
        clear_screen()
        DelRecipe, index = select_recipe()

        # Absicherung Absturz wegen Schleife bei leerem Rezeptbuch
        if not DelRecipe:
            clear_screen()
            return

        clear_screen()

        # Schleife für Sicherheitsfrage
        while True:
            print('\n=== Rezept löschen ===')
            # Sicherheitsfrage
            decide = input(f'"{DelRecipe['name']}" wirklich löschen? (j/n): ')
            if decide.lower().strip() == "j":
                ListOfRecipes = load_recipes()

                # löschen über Position Liste
                ListOfRecipes.pop(index)
                save_recipes(ListOfRecipes)
                print('\n--- Rezept erfolgreich gelöscht --- \n')
                break
                
            elif decide.strip().lower() == "n":
                print ('\n--- Löschvorgang abgebrochen --- \n')
                break
                            
            else: print('\n[ERROR] Eingabe ungültig ! (gib "J" oder "N" ein): ')

        # Auswahl Text im Menu
        choice = choose_next_action({
            "1": "Rezeptliste ansehen",
            "2": "Weiteres Rezept löschen",
            "3": "Zurück zum Hauptmenü"
        })

        if choice == "1":
            show_recipes()
            return

        if choice == "2":
            continue

        if choice == "3":
            clear_screen()
            return