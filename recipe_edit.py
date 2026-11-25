from storage import load_recipes
from storage import save_recipes
from recipe_display import select_recipe
from recipe_features import user_input2_favorites
from recipe_features import ask_recipe_allergies
from recipe_input import ask_ingredients, ask_portions, ask_ingredient_amount, ask_ingredient_name, ask_ingredient_unit, ask_recipe_name
from navigation import clear_screen, choose_next_action

def edit_recipe(selected_index=None):
    while True:
        clear_screen()

        if selected_index is None:
            edit, index = select_recipe()
        else:
            index = selected_index
            edit = load_recipes()[index]
            selected_index = None

        if not edit:
            return 

        clear_screen()

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
                print(f'- [{ingredient['name']} {ingredient['amount']:g} {ingredient['unit']}]')
            
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
                edit['name'] = ask_recipe_name()

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('--- Rezeptname erfolgreich aktualisiert ---\n')
                break

            elif select == "2" or select == "2.":
                edit['portions'] = ask_portions()

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('--- Portionen erfolgreich aktualisiert ---\n')
                break

            elif select == "3" or select == "3.":
                edit['ingredients'] = edit['ingredients'] + ask_ingredients()

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('--- Zutaten erfolgreich hinzugefügt ---')
                break

            elif select == "4" or select == "4.":
                print(f'\n=== Zutaten "{edit['name']}" entfernen ===')
                for no, ingredients in enumerate(edit['ingredients']):
                    print(f'{no+1}. [{ingredients['name']} {ingredients['amount']} {ingredients['unit']}]')

                deleted = False
                
                while True:
                    number = input('\nWähle die Zeile, die du entfernen willst (oder wähle "Z" für zurück): ').lower().strip()
                    if number == "z":
                        break
                    
                    if number .isdigit():
                        number = int(number)-1
                        
                        if 0 <= number < len(edit['ingredients']):     

                            selected_ingredient = edit['ingredients'][number]
                            row = input(f'"{selected_ingredient['name']} {selected_ingredient['amount']} {selected_ingredient['unit']}" wirklich löschen? (j/n): ').lower().strip()
                            while row not in ("j", "n"):
                                row = input('[ERROR] Ungültige Eingabe! Wähle J oder N: ').lower().strip()

                            if row == "n":
                                break

                            elif row == "j":
                                if len(edit['ingredients']) == 1:
                                    print("[ERROR] Die letzte Zutat darf nicht gelöscht werden.")
                                    continue

                                delete = edit['ingredients'].pop(number)
                                print(f'\n--- "{delete['name']} {delete['amount']} {delete['unit']}" erfolgreich entfernt ---\n')

                                recipes = load_recipes()
                                recipes[index] = edit
                                save_recipes(recipes)
                                deleted = True 

                            break         

                        else: print('[ERROR] Eingabe ungültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')
                    else: print('[ERROR] Eingabe ungültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')
                                          
                if deleted:
                    break

                clear_screen()

            elif select == "5" or select == "5.":
                print(f'\n=== Zutaten "{edit['name']}" ändern ===')
                for no, ingredients in enumerate(edit['ingredients']):
                    print(f'{no+1}. [{ingredients['name']} {ingredients['amount']} {ingredients['unit']}]')

                changed = False
                
                while True:
                    number = input('\nWähle die Zeile, die du ändern willst (oder wähle "Z" für zurück): ').lower().strip()
                    if number == "z":
                        break
                    
                    if number .isdigit():
                        number = int(number)-1
                        
                        if 0 <= number < len(edit['ingredients']):     
                            

                            row = edit['ingredients'][number]          
                            print(f'[{row['name']} {row['amount']} {row['unit']}]')

                            row['name'] = ask_ingredient_name()
                            print(f'Gespeicherte Änderung: [{row['name']}]')

                            row['amount'] = ask_ingredient_amount()
                            print(f'Gespeicherte Änderung: [{row['name']} {row['amount']}]')           

                            row['unit']= ask_ingredient_unit()
                            print(f'Gespeicherte Änderung: [{row['name']} {row['amount']} {row['unit']}]') 
                            print('\n--- Zutaten erfolgreich aktualisiert ---\n')

                            recipes = load_recipes()
                            recipes[index] = edit
                            save_recipes(recipes)
                            changed = True

                            break         

                        else: print('[ERROR] Eingabe ungültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')
                    else: print('[ERROR] Eingabe ungültig ! Siehe Zutatenliste und gib die ZAHL der gewünschten ZEILE ohne Punkt ein.')

                if changed:
                    break

                clear_screen()
              
            elif select == "6" or select == "6.":
                edit['allergies'] = ask_recipe_allergies()       

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                print('---Allergien erfolgreich aktualisiert ---\n')
                break
            
            elif select == "7" or select == "7.":        
  
                # Update Anpassung neue Version favorites
                user_input2 = user_input2_favorites()
                if user_input2.upper().strip() == "H" or user_input2.upper().strip() == "1." or user_input2.upper().strip() == "1":
                    print('--- Favorit erfolgreich aktualisiert ---\n')
                    edit["favorite"] = True
                    
                
                elif user_input2.upper().strip() == "E" or user_input2.upper().strip() == "2." or user_input2.upper().strip() == "2":
                    edit["favorite"] = False
                    print('--- Favorit erfolgreich aktualisiert ---\n')

                recipes = load_recipes()
                recipes[index] = edit
                save_recipes(recipes)
                break
                            
            elif select == "8" or select == "r" or select == "8.":
                break 

            elif select == "9" or select == "h" or select == "9.":
                clear_screen()
                return

            else: print('\n[ERROR] Eingabe ungültig ! (gib eine Zahl zwischen 1-9 ein) ')

        if select in ("8", "8.", "r"):
            continue

        choice = choose_next_action({
            "1": "Weiteres Rezept bearbeiten",
            "2": "Bearbeitetes Rezept anzeigen",
            "3": "Zurück zum Hauptmenü"
        })

        if choice == "2":
            from recipe_display import details_recipe
            clear_screen()
            details_recipe(load_recipes()[index])

            choice = choose_next_action({
                "1": "Weiteres Rezept bearbeiten",
                "2": "Zurück zum Hauptmenü"
            })

            if choice == "2":
                clear_screen()
                return

        if choice == "3":
            clear_screen()
            return