# Restart - New Version 2 of edit_recipe

from storage import load_recipes
from storage import save_recipes
from recipe_tools import select_recipe
from recipe_tools import details_recipe
from recipe_display import show_recipes
from recipe_features import user_input2_favorites
from recipe_features import user_input_allergies
from recipe_features import ask_recipe_allergies

def edit_recipe():
    while True:
        edit = select_recipe()

        if not edit:
            return

        # Schleife für 6. und 7.
        #while True:

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
        print('7. zurück zum Hauptmenü\n')

        # Schleife für 6. und 7.
        while True:
            select = input('Was möchtest du bearbeiten? ')
        
            if select == "1":
                old_name = edit['name']
                edit['name'] = input('NEUER Rezeptname: ')

                recipes = load_recipes()
                for recipe in recipes:
                    if recipe['name'] == old_name:
                        recipe['name'] = edit['name']

                save_recipes(recipes)
                print('\n--- Rezeptname erfolgreich aktualisiert ---\n')

            elif select == "2":
                old_portions = edit['portions']
                edit['portions'] = input('NEUE Anzahl Portionen: ')
                edit['portions'] = int(edit['portions'])

                recipes = load_recipes()
                for recipe in recipes:
                    if recipe['portions'] == old_portions:
                        recipe['portions'] = edit['portions']

                save_recipes(recipes)        
                print('--- Portionen erfolgreich aktualisiert ---')

            elif select == "3":
                print('nv')

            elif select == "4":
                ask_recipe_allergies() # Prüfen: Favoriten werden nicht gespeichert                
            
            elif select == "5":
                #user_input2_favorites()
                print('Favorit bearbeiten ist noch nicht verfügbar.')
            
            elif select == "6":
                break 

            elif select == "7": 
                return

            else: print('\n[ERROR] Eingabe ungültig ! (gib eine Zahl zwischen 1-7 ein) ')



# Testmode
edit_recipe()