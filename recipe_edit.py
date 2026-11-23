from storage import load_recipes
from storage import save_recipes
from recipe_display import select_recipe
from recipe_features import user_input2_favorites
from recipe_features import ask_recipe_allergies
from recipe_input import ask_ingredients

def edit_recipe():
    while True:
        edit, index = select_recipe()

        if not edit:
            return 

        # Schleife für Menünavigation
        while True:

            # Menüauswahl
            print(f'\n=== Rezept "{edit['name']}" bearbeiten ===')
            print(f'1. REZEPTNAME ändern [{edit['name']}]' )
            print(f'2. PORTIONEN ändern [{edit['portions']}]')

            print('\n3. ZUTATEN hinzufügen')
            print('4 ZUTATEN entfernen')

            print('\n5. ZUTATEN ändern:')
            for ingredient in edit['ingredients']:
                print(f'- [{ingredient['name']} {ingredient['amount']:.0f} {ingredient['unit']}]')
            
            print('\n6. ALLERGIEN ändern ', end = '')
            if not edit['allergies']:
                print('[keine erfasst]')
            for allergies in edit['allergies']:
                print(f'[{allergies}]', end = ' ')
            
            print('\n7. FAVORIT ', end='')
            if edit['favorite'] == True:
                print('[ja]')
            else: print('[nein]')
            
            print('\n8. zurück zur REZEPTLISTE [R]')
            print('9. zurück zum HAUPTMENÜ [H]')

        
            select = input('\nWähle anhand der Nummer was du bearbeiten möchtest: ').strip().lower()
        
            if select == "1" or select == "1.":
                edit['name'] = input('\nNEUER Rezeptname: ')

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('--- Rezeptname erfolgreich aktualisiert ---\n')
                input('Klicke Enter, um zurück zur Rezeptliste zu gelangen: ')
                break

            elif select == "2" or select == "2.":
                edit['portions'] = input('\nNEUE Anzahl Portionen: ')
                edit['portions'] = int(edit['portions'])

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('--- Portionen erfolgreich aktualisiert ---\n')
                input('Klicke Enter, um zurück zur Rezeptliste zu gelangen: ')
                break

            elif select == "3" or select == "3.":
                edit['ingredients'] = edit['ingredients'] + ask_ingredients()

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('--- Zutaten erfolgreich hinzugefügt ---')
                input('Klicke Enter, um zurück zur Rezeptliste zu gelangen: ')
                break

            elif select == "4" or select == "4.":
                print(f'\n=== Zutaten "{edit['name']}" ändern ===')
                for no, ingredients in enumerate(edit['ingredients']):
                    print(f'{no+1}. [{ingredients['name']} {ingredients['amount']} {ingredients['unit']}]')
                
                while True:
                    number = input('\nWähle die Zeile, die du ändern willst (oder wähle "Z" für zurück): ').lower().strip()
                    if number == "z":
                        break
                    
                    if number .isdigit():
                        number = int(number)-1
                        
                        if 0 <= number < len(edit['ingredients']):     

                            row = input(f'"{ingredients['name']} {ingredients['amount']} {ingredients['unit']}" wirklich löschen? (j/n): ').lower().strip()
                            while row != "j" and row != "n":
                                print('[ERROR] Eingabe ungültig ! wähle "J" oder "N"')
                                break

                            if row == "n":
                                break

                            elif row == "j":
                                delete = edit['ingredients'].pop(number)
                                print(f'\n--- "{delete['name']} {delete['amount']} {delete['unit']}" erfolgreich entfernt ---\n')

                                recipes = load_recipes()
                                recipes[index] = edit
                                save_recipes(recipes) 

                            input('Klicke Enter, um zurück zum Bearbeitungsmenü zu gelangen: ')
                            break         

                        else: print('[ERROR] Eingabe gültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')
                    else: print('[ERROR] Eingabe ungültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')
                                          


            elif select == "5" or select == "5.":
                print(f'\n=== Zutaten "{edit['name']}" ändern ===')
                for no, ingredients in enumerate(edit['ingredients']):
                    print(f'{no+1}. [{ingredients['name']} {ingredients['amount']} {ingredients['unit']}]')
                
                while True:
                    number = input('\nWähle die Zeile, die du ändern willst (oder wähle "Z" für zurück): ').lower().strip()
                    if number == "z":
                        break
                    
                    if number .isdigit():
                        number = int(number)-1
                        
                        if 0 <= number < len(edit['ingredients']):     
                            

                            row = edit['ingredients'][number]          
                            print(f'[{row['name']} {row['amount']} {row['unit']}]')

                            row['name'] = input('\nZutat unbenennen: ')
                            print(f'Gespeicherte Änderung: [{row['name']}]')

                            row['amount'] = input('\nMenge ändern: ')
                            row['amount'] = int(row['amount'])
                            print(f'Gespeicherte Änderung: [{row['name']} {row['amount']}]')           

                            row['unit']= input('\nEinheit ändern (g / ml / Stück): ')
                            print(f'Gespeicherte Änderung: [{row['name']} {row['amount']} {row['unit']}]') 
                            print('\n--- Zutaten erfolgreich aktualisiert ---\n')

                            recipes = load_recipes()
                            recipes[index] = edit
                            save_recipes(recipes) 

                            input('Klicke Enter, um zurück zum Bearbeitungsmenü zu gelangen: ')
                            break         

                        else: print('[ERROR] Eingabe gültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')
                    else: print('[ERROR] Eingabe ungültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')
              
            elif select == "6" or select == "6.":
                edit['allergies'] = edit['allergies'] + ask_recipe_allergies()         

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('---Allergien erfolgreich aktualisiert ---\n')
                input('Klicke Enter, um zurück zur Rezeptliste zu gelangen: ')
                break
            
            elif select == "7" or select == "7.":
                #edit['favorite'] = user_input2_favorites()

# Teile kopiert aus Funktion edit_favorite + Anpassung variable edit statt recipe
#def edit_favorites():
    #recipes = load_recipes()
    #show_favorites = input("1 = Favoriten anzeigen, 2 = Favoriten bearbeiten (Bitte Zahl 1 oder 2 angeben): ")
    #if show_favorites == "2":
        #for recipe in recipes:
        #    print(f"Rezept: {recipe['name']}; ID: {recipe['id']}; Favorites: {recipe['favorite']}")
        #user_input1 = user_input1_favorites()
                user_input2 = user_input2_favorites()
                #for recipe in recipes:
                    #if user_input1 == str(recipe["id"]):
                if user_input2.lower().strip() == "hinzufügen":
                    edit["favorite"] = True
                    print(f"Das Rezept für {edit['name']} wurde zu den Favoriten hinzugefügt")
                elif user_input2.lower().strip() == "entfernen":
                    edit["favorite"] = False
                    print(f"Das Rezept für {edit['name']} wurde von den Favoriten entfernt")
                #save_recipes(recipes)
    #else:
     #   get_favorites()



                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('--- Favorit erfolgreich aktualisiert ---\n')

                print('\n(Favorit bearbeiten ist noch nicht verfügbar.)\n')
            
            elif select == "8" or select == "r" or select == "8.":
                break 

            elif select == "9" or select == "h" or select == "9.": 
                return

            else: print('\n[ERROR] Eingabe ungültig ! (gib eine Zahl zwischen 1-8 ein) ')

# noch offen:
# Favorit wird nicht gespeichert