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
        print('\n--- Rezeptdetails ---')

        select_id = input("Wähle Rezept-Nr.: ") # Prüfung Fehlermeldung
        select_id = int(select_id)
                
        for recipe in recipes:
            if select_id == recipe['id']:
                break

        # Detailansicht, wird wegen Mehrfachbrauch noch in eine Funktion umgewandelt
        print(f"\n--- {recipe['name']} ---")
        print(f"(Rezept für {recipe['portions']} Portionen)")
        print(f"\nZutaten:")
        print(f"- {ingredients['amount']} {ingredients['unit']} {ingredients['name']}")
        



              









# Testmode
edit_recipe() 



    
#grober Plan:

# Auswahlmenü
# Eigenschaftsmenü
# Änderungsparameter
# Bestätigung








