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
            print("f{recipe['id]}, {recipe['name']}")
            
   



    
#grober Plan:

# Auflistung Rezept
# Auswahlmenü
# Eigenschaftsmenü
# Änderungsparameter
# Bestätigung








