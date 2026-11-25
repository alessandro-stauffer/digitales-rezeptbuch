from storage import load_recipes
from navigation import clear_screen, choose_next_action

# Funktion REZEPTE ANZEIGEN
def show_recipes():

    # Schleife für R am Schluss
    while True:
        clear_screen()

        # Aktivierung Funktion Rezeptauswahl
        SelectRecipe, index = select_recipe()

        # Absicherung Absturz wegen Schleife bei leerem Rezeptbuch
        if not SelectRecipe:
            clear_screen()
            print("Es sind noch keine Rezepte vorhanden.")
            return

        clear_screen()
        details_recipe(SelectRecipe)
        print('\n=== VIEL FREUDE BEIM KOCHEN ! ===\n')
            
        # Schleife, um mehrere Rezepte nacheinander anzuzeigen
        choice = choose_next_action({
            "1": "Weiteres Rezept anzeigen",
            "2": "Dieses Rezept bearbeiten",
            "3": "Dieses Rezept skalieren",
            "4": "Zurück zum Hauptmenü"
        })

        if choice == "2":
            from recipe_edit import edit_recipe
            edit_recipe(index)
            return

        if choice == "3":
            from recipe_tools import scale_recipe_menu
            scale_recipe_menu(index)
            return

        if choice == "4":
            clear_screen()
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
        print(f'- {ingredients['name']} {ingredients['amount']:g} {ingredients['unit']}')

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
