# Tool: Herstellung Verbindung json
import json

from storage import load_recipes

def edit_recipe():
    recipes = load_recipes()

    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return
    
    else:
        print('\n=== Deine Rezepte ===')
        for recipe in recipes:
            print(f"{recipe['id']} {recipe['name']}")
        print()

        select_id = input("Wähle Rezept-Nr.: ")









# Testmode
edit_recipe() 



    
#grober Plan:

# Auswahlmenü
# Eigenschaftsmenü
# Änderungsparameter
# Bestätigung








