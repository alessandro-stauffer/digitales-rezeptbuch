# Rezept anzeigen Funktion auslagern, doppelte Codes bei Anzeigen von Rezepten

from storage import load_recipes

# Aufbau Funktion (finde geeigneten Funktionsname) -- OK behalten!
def select_recipe ():
    ListOfRecipes = load_recipes()

    # Prüfung Rezeptbuch ist leer
    if not ListOfRecipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    while True:
        print ('\n=== Rezeptliste ===')

        # Menünavigation über Nummerierung
        for index, recipe in enumerate (ListOfRecipes):
            print(f'{index+1}. {recipe['name']}')

        
        while True:
            UsersChoice = input('\nWähle Rezept-Nr.: ')

            # Prüfung, ob Eingabe eine Zahl ist
            if UsersChoice .isdigit():

                # Umwandlung Eingabe von str in int
                UsersChoice = int(UsersChoice)

                # Range Nummerierung Rezepte
                if 1 <= UsersChoice <= len(ListOfRecipes):

                    # neue Variable (sonst wird UsersChoice überschrieben)
                    SelectedRecipe = ListOfRecipes[UsersChoice-1]

                    # nur für Test
                    print(f'{UsersChoice} {SelectedRecipe['name']}')
                    break

                # Fehleingaben
                else: print(' \n--- kein Rezept gefunden --- \n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gebe die Nummer des gewünschten Rezepts ein)') # falsche Zahl
            else: print ('\n--- kein Rezept gefunden ---\n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gib eine gültige ZAHL ein)') # Buchstaben statt Zahl
                            
                





select_recipe()

# ausstehende To Do's:
# Variabeln unbenennen - zu viel Ähnliches - ERLEDIGT !
# Fehleingaben - ERLEDIGT !


