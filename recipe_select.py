from storage import load_recipes

def select_recipe ():
    ListOfRecipes = load_recipes()

    # Prüfung Rezeptbuch ist leer
    if not ListOfRecipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

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

                # Variable benennen für den Einbau in andere Funktionen
                return SelectedRecipe

            # Fehleingaben
            else: print(' \n--- kein Rezept gefunden --- \n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gebe die Nummer des gewünschten Rezepts ein)') # falsche Zahl
        else: print ('\n--- kein Rezept gefunden ---\n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gib eine gültige ZAHL ein)') # Buchstaben statt Zahl




