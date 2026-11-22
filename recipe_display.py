from storage import load_recipes

# Funktion REZEPTE ANZEIGEN
def show_recipes():

    # Schleife für R am Schluss
    while True:

        # Aktivierung Funktion Rezeptauswahl
        SelectRecipe, index = select_recipe()

        # Absicherung Absturz wegen Schleife bei leerem Rezeptbuch
        if not SelectRecipe:
            return

        details_recipe(SelectRecipe)
        print('\n=== VIEL FREUDE BEIM KOCHEN ! ===\n')
            
        # Schleife für weiterfahren Menüauswahl r oder h
        while True:
            move = input('wähle "R" für Rezeptliste oder "H" für Hauptmenü: ').strip().lower()

            # Schleife nach ungültiger Eingabe
            while move != "r" and move != "h":
                move = input('\n[ERROR] Eingabe ungültig ! (gib "R" oder "H" ein): ').lower().strip()

            if move == "r":
                break
            elif move == "h":
                return

            

# from removed file recipe_select.py: FUNKTION REZEPTLISTE
def select_recipe ():
    ListOfRecipes = load_recipes()

    # Prüfung Rezeptbuch ist leer
    if not ListOfRecipes:
        print('\n--- keine Rezepte vorhanden ---\n')

        # 2x None, weil return 2x Variabeln herausgibt
        return None, None

    print ('\n=== Rezeptliste ===')

    # Menünavigation über Nummerierung
    for index, recipe in enumerate (ListOfRecipes):
        print(f'{index+1}. {recipe['name']}')
    
    # Schleife für Fehleingaben
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

                # Variable Endwert select_recipe
                return SelectedRecipe, UsersChoice-1

            # Fehleingaben
            else: print(' \n--- kein Rezept gefunden --- \n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gebe die Zahl des gewünschten Rezepts ein)') # falsche Zahl
        else: print ('\n--- kein Rezept gefunden ---\n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gib eine gültige ZAHL ohne Punkt ein)') # Buchstaben statt Zahl



# from removed file recipe_details.py: FUNKTION REZEPTDETAILS
def details_recipe(details):

    if not details:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    print(f'\n=== Rezept: {details['name']} ===')
    print(f'Portionen: {details['portions']}')
    print('\nZutaten:')

    for ingredients in details['ingredients']:
        print(f'- {ingredients['name']} {ingredients['amount']:.0f} {ingredients['unit']}')

    if not details['allergies']:
        print('\nAllergien: keine erfasst')

    else:
        print(f'\nAllergien: ', end = '')
        for allergies in details['allergies']:
            print(f'{allergies}', end = ' ')
        print()

    if details['favorite'] == True:
        print('Favorit: ja')
    else: print('Favorit: nein')
