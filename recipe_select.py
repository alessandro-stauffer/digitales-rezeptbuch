# Rezept anzeigen Funktion auslagern, doppelte Codes bei Anzeigen von Rezepten

from storage import load_recipes

# Aufbau Funktion (finde geeigneten Funktionsname)
def select_recipe ():
    recipes = load_recipes()

    # Prüfung Rezeptbuch ist leer
    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

# später testen ob auch hier while True: Schleife hier Sinn macht
    else:
        print ('\n=== Rezeptliste ===')

        # Menünavigation über Nummerierung
        for index, recipe in enumerate (recipes):
            print(f'{index+1}. {recipe['name']}')


        select = input('\nWähle Rezept-Nr.: ')

        # Prüfung, ob Eingabe eine Zahl ist
        if select .isdigit():

            # Umwandlung Eingabe von str in int
            select = int(select)

            # Range Nummerierung Rezepte
            if 1 <= select <= len(recipes):
                number = recipes[select-1]
                

    # nur für TEst
                print(f'{select} {number['name']}')



select_recipe()

# ausstehende To Do's:
# Funktion unbenennen ? - Name nicht ideal, sorgt für Verwirrung !
# Variabeln unbenennen - zu viel Ähnliches
# Fehleingaben



