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
        edit, index = select_recipe()

        if not edit:
            return 

        # Schleife für 6. und 7.
        #while True:

            #print('\n"Was möchtest du ändern?\n')
            
        # Menüauswahl
        print(f'\n=== Rezept "{edit['name']}" bearbeiten ===')
        print(f'\n1. REZEPTNAME ändern [{edit['name']}]' )
        print(f'2. PORTIONEN ändern [{edit['portions']}]')
        
        print('\n3. ZUTATEN ändern:')
        for ingredient in edit['ingredients']:
            print(f'- [{ingredient['name']} {ingredient['amount']:.0f} {ingredient['unit']}]')
        
        print('\n4. ALLERGIEN ändern ', end = '')
        if not edit['allergies']:
            print('[keine erfasst]')
        for allergies in edit['allergies']:
            print(f'{allergies}', end= '')
        
        print('5. FAVORIT ', end='')
        if edit['favorite'] == True:
            print('[ja]')
        else: print('[nein]')
        
        print('\n6. zurück zur REZEPTLISTE [R]')
        print('7. zurück zum HAUPTMENÜ [H]\n')

        # Schleife für Menünavigation
        while True:
            select = input('Wähle anhand der Nummer was du bearbeiten möchtest: ').strip().lower()
        
            if select == "1" or select == "1.":
                edit['name'] = input('\nNEUER Rezeptname: ')

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)

                print('--- Rezeptname erfolgreich aktualisiert ---\n')

            elif select == "2":
                edit['portions'] = input('\nNEUE Anzahl Portionen: ')
                edit['portions'] = int(edit['portions'])

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)

                print('--- Portionen erfolgreich aktualisiert ---\n')

            elif select == "3":
                print('nv')

            elif select == "4":
                ask_recipe_allergies() # Prüfen: Favoriten werden nicht gespeichert                
            
            elif select == "5" or select == "5.":
                #user_input2_favorites()
                print('\n(Favorit bearbeiten ist noch nicht verfügbar.)\n')
            
            elif select == "6" or select == "r" or select == "6.":
                break 

            elif select == "7" or select == "h" or select == "7.": 
                return

            else: print('\n[ERROR] Eingabe ungültig ! (gib eine Zahl zwischen 1-7 ein) ')



# Testmode
edit_recipe()