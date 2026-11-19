# Rezept anzeigen Funktion auslagern, doppelte Codes bei Anzeigen von Rezepten

from storage import load_recipes

def select_recipe ():
    recipes = load_recipes()

    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    else:
        print ('\n=== Rezeptliste ===')

        for index, recipe in enumerate (recipes):
            print(f'{index+1}. {recipe['name']}')
        print()


