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
        
        print('\n4. ALLERGIEN überschreiben ', end = '')
        if not edit['allergies']:
            print('[keine erfasst]')
        for allergies in edit['allergies']:
            print(f'[{allergies}]', end = ' ')
        
        print('\n5. FAVORIT ', end='')
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

            elif select == "2" or select == "2.":
                edit['portions'] = input('\nNEUE Anzahl Portionen: ')
                edit['portions'] = int(edit['portions'])

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)

                print('--- Portionen erfolgreich aktualisiert ---\n')

            elif select == "3":
                #print('\nZutaten bearbeite ist noch nicht verfügbar.')

                print(f'\n=== Zutaten "{edit['name']}" ändern ===')
                for no, ingredients in enumerate(edit['ingredients']):
                    print(f'{no+1}. {ingredients['name']} {ingredients['amount']} {ingredients['unit']}')

                number = input('\nWähle die Zeile, die du ändern willst: ')
                number = int(number)-1

                row = edit['ingredients'][number]          
                print(f'{row['name']} {row['amount']} {row['unit']}')

                row['name'] = input('\nZutat unbenennen: ')
                print(f'Gespeicherte Änderung: {row['name']}')

                row['amount'] = input('\nMenge ändern: ')
                row['amount'] = int(row['amount'])
                print(f'Gespeicherte Änderung: {row['name']} {row['amount']}')           

                row['unit']= input('\nEinheit ändern (g / ml / Stück): ')
                print(f'Gespeicherte Änderung: {row['name']} {row['amount']} {row['unit']}') 
                print('\n--- Zutaten erfolgreich aktualisiert ---\n')

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
    
                
                #for ingredient in edit['ingredients']:
                 #   edit['ingredients'] = enumerate (ingredient['name'] ingredient['amount] ingredient['unit'])



            elif select == "4" or select == "4.":
                edit['allergies'] = ask_recipe_allergies()         

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('---Allergien erfolgreich aktualisiert ---\n')
            
            elif select == "5" or select == "5.":
                #edit['favorite'] = user_input2_favorites()

                #recipes = load_recipes()
                #recipes[index] = edit
                #save_recipes(recipes)
                #print('--- Favorit erfolgreich aktualisiert ---\n')

                print('\n(Favorit bearbeiten ist noch nicht verfügbar.)\n')
            
            elif select == "6" or select == "r" or select == "6.":
                break 

            elif select == "7" or select == "h" or select == "7.": 
                return

            else: print('\n[ERROR] Eingabe ungültig ! (gib eine Zahl zwischen 1-7 ein) ')

# noch offen:
# Menü 3 Zutaten fehlt noch - ERLEDIGT !
# Allergien eingebaut, aber als Überschreibung anstatt Änderung drin
# Favorit wird nicht gespeichert
