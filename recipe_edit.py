# Tool: Herstellung Verbindung json
import json

from storage import load_recipes
from storage import save_recipes

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
        select_id = input("Wähle Rezept-Nr.: ")
        select_id = int(select_id)
                
        for recipe in recipes:
            if select_id == recipe['id']:
                break

        # Detailansicht, wird wegen Mehrfachbrauch noch in eine Funktion umgewandelt
        print(f"\n--- {recipe['name']} ---")
        print(f"(Rezept für {recipe['portions']} Portionen)")
        print(f"\nZutaten:")
        for ingredient in recipe['ingredients']:
            print(f"- {ingredient['amount']} {ingredient['unit']} {ingredient['name']}") 
        
        print('\nDetail bearbeiten:')
        print(f"(1) Rezeptname: {recipe['name']}")
        print(f"(2) Portionen: {recipe['portions']}")
        print(f"(3) Zutaten bearbeiten")

     #   for index in range(len(recipe['ingredients'])):
      #      ingredient = recipe['ingredients'][index]
       #     for 
        #        print(f"{recipe['ingredients'][index]}") # hier stimmt was nicht

        # Änderung Rezeptname
        choice = input("\nWähle Detail-Nr.: ")
        print()
        if choice == "1":
            recipe['name'] = input("NEUER Rezeptname: ")
            save_recipes(recipes)
            print("\n--- Der Rezeptname wurde erfolgreich aktualisiert. ---\n")

        # Änderung Anzahl Portionen
        elif choice == "2":
            recipe['portions'] = input('NEUE Anzahl Portionen: ')
            recipe['portions'] = int(recipe['portions'])
            save_recipes(recipes)
            print('\n--- Die Anzahl Portionen wurde erfolgreich korrigiert. ---\n')

        # Änderung Zutaten
        elif choice == "3":
            print("Zutaten bearbeiten:")
            for index in range(len(recipe['ingredients'])):
                ingredient = recipe['ingredients'][index]
                print(f"({index+1}) {ingredient['amount']} {ingredient['unit']} {ingredient['name']}")

            ingredient_choice = input("\nWähle Zutat-Nr: ")
            ingredient_choice = int(ingredient_choice)-1
            ingredient = recipe['ingredients'][ingredient_choice]
            
            print("(1) Zutat(name)")
            print("(2) Menge")
            print("(3) Einheit")
            nd_choice = input("Wähle die Änderungsposition (1-3): ")

            if nd_choice == "1":
                ingredient['name'] = input("KORREKTUR Zutat: ")
                save_recipes(recipes)
                print('\n--- Name der Zutat erfolgreich geändert ---\n')

            elif nd_choice == "2":
                ingredient['amount'] = input("KORREKTUR Menge: ")
                ingredient['amount'] = float(ingredient['amount'])
                save_recipes(recipes)
                print('\n--- Menge erfolgreich geändert ---\n')

            elif nd_choice == "3":
                ingredient['unit'] = input("KORREKTUR Einheit: ")
                save_recipes(recipes)
                print('\n--- Einheit erfolgreich geändert ---\n')

            else: print("Eingabe ungültig ! Gib eine gültige Zahl ein. ")
        else: print("Eingabe ungültig ! Gib eine gültige Zahl ein. ")
    #else: print("Eingabe ungültig ! Gib eine gültige Zahl ein. ")


                




            










       





              









# Testmode
edit_recipe() 



    
#grober Plan:

# Auswahlmenü
# Eigenschaftsmenü
# Änderungsparameter
# Bestätigung








