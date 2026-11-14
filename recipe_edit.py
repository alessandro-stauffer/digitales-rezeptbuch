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

        select_id = int(input("Wähle Rezept-Nr.: ")) # Prüfung Fehlermeldung
       
    
        for recipe in recipes
            if select_id == recipe['id']

        # Detailansicht, wird wegen Mehrfachbrauch noch in eine Funktion umgewandelt
        print('\n--- Rezeptdetails ---')
        print(f"{recipe['name']}")
              









# Testmode
edit_recipe() 



    
#grober Plan:

# Auswahlmenü
# Eigenschaftsmenü
# Änderungsparameter
# Bestätigung








