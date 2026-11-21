# Restart - New Version 2 of edit_recipe

from storage import load_recipes
from storage import save_recipes
from recipe_tools import select_recipe
from recipe_tools import details_recipe
from recipe_display import show_recipes

def edit_recipe():
    while True:
        edit = select_recipe()

        if not edit:
            return

        # Schleife für 6. und 7.
        while True:

            #print('\n"Was möchtest du ändern?\n')
            
            # Menüauswahl
            print(f'\n=== Rezept "{edit['name']}" bearbeiten ===')
            print(f'\n1. Rezeptname ändern [{edit['name']}]' )
            print(f'2. Portionen ändern [{edit['portions']}]')
            
            print('\n3. Zutaten ändern:')
            for ingredient in edit['ingredients']:
                print(f'- [{ingredient['name']} {ingredient['amount']:.0f} {ingredient['unit']}]')
            
            print('\n4. Allergien ändern ', end = '')
            if not edit['allergies']:
                print('[keine erfasst]')
            for allergies in edit['allergies']:
                print(f'{allergies}', end= '')
            
            print('5. Favorit ', end='')
            if edit['favorite'] == True:
                print('[ja]')
            else: print('[nein]')
            
            print('\n6. zurück zur Rezeptauswahl')
            print('7. zurück zum Hauptmenü')

            select = input('\nWas möchtest du bearbeiten? ')
            
            if select == "6":
                break 

            if select == "7": 
                return

            else: print('\n[ERROR] Eingabe ungültig ! (gib eine Zahl zwischen 1-7 ein): ')



# Testmode
edit_recipe()