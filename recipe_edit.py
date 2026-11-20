# Restart - New Version 2 of edit_recipe

from storage import load_recipes
from storage import save_recipes
from recipe_tools import select_recipe

def edit_recipe():
    while True:
        edit = select_recipe()

        if not edit:
            return

        # Schleife für 6. und 7.
        while True:

            # Menüauswahl
            print(f'\n=== Rezept "{edit['name']}" bearbeiten ===')
            print('1. Rezeptname ändern')
            print('2. Portionen ändern')
            print('3. Zutaten ändern')
            print('4. Allergien ändern')
            print('5. Favorit setzen')
            print('6. zurück zur Rezeptauswahl')
            print('7. zurück zum Hauptmenü')

            
            select = input('\nWähle Bearbeitungsmenü: ')
            
            if select == "6":
                break 

            if select == "7": 
                return

            # else: print('\n[ERROR] Eingabe ungültig ! (gib eine Zahl zwischen 1-7 ein): ')



# Testmode
edit_recipe()