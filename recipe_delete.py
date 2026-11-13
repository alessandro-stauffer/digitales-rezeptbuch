# Tool: Herstellung Verbindung json
import json

# Tool: Rezepte laden
from storage import load_recipes

# Tool: Rezepte speichern
from storage import save_recipes

def delete_recipe(recipes):
    recipes = load_recipes()

    # Status Rezeptbuch ist leer ()
    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    # vorhandene Rezepte ()
    print('\n=== Deine Rezepte ===')
    for i, recipe in enumerate (recipes):
        print(i+1, recipe["name"])

    # Rezept fürs Löschen wählen
    number = input('\nWähle Rezept-Nr. zum löschen: ')

# Prüfung int & Umwandlung Zahl ()
    if number.isdigit():
        number = int(number)

        # Prüfung Rezeptliste Anz. ()
        if 1 <= number <= len(recipes):
            selected_recipe = recipes[number - 1]   

            # Sicherheitsfrage
            decide = input(f'\n{selected_recipe['name']} wirklich löschen? (j/n): '):
            if decide.lower().strip() == "j":

                # löschen über Position Liste
                recipe.pop(number -1)
                save_recipes(recipes)
                print('\n--- Rezept erfolgreich gelöscht --- \n')
            else: print ('\n--- Löschvorgang abgebrochen --- \n')
        else: print ('\n--- kein Rezept gefunden --- \n')
    else: print('\n--- kein Rezept gefunden ---\n')




                 




# weiteres Vorgehen nachdem Rezept ausgewählt

 #def recipe_delete(decision,input):
#decision = input("Bist du dir ganz sicher, dass du das Rezept löschen möchtest? ").strip().lower()
#if decision == "j":
 #   print("Alles klar, das Rezept wurde erfolgreich gelöscht !")

#elif decision == "n":
 #   print("Puuh, Glück gehabt, nichts ist gelöscht oder verloren :)")

#else: print('Oh, tut mir Leid, ich habe deine Eingabe nicht verstanden - antworte am besten mit "j" oder "n" ;) ')




 # Funktion Rezepte einfügen
#from recipe_management import add_recipe_id # die Rezept ID Auswahl


