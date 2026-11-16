# Tool: Rezepte laden
from storage import load_recipes

# Funktion Rezepte anzeigen
def show_recipes():
    recipes = load_recipes()

    # Status Rezeptbuch ist leer
    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    # Schleife zurück bei Fehleingabe
    while True:

        # vorhandene Rezepte
        print('\n=== Deine Rezepte ===')

        # i = Startpunkt
        for index, recipe in enumerate (recipes):

            # +1 wegen Nummerierung ab 0
            print(f'{index+1}. {recipe["name"]}')

        # Rezept öffnen
        while True:
            number = input('\nWähle Rezept-Nr.: ')

            # Prüfung int
            if number.isdigit():

                # Umwandlung Zahl
                number = int(number)

                # Prüfung Rezeptliste Anz.
                if 1 <= number <= len(recipes):
                    selected_recipe = recipes[number - 1]

                    # Detailansicht
                    print('\n === Rezeptdetails ===\n')

                    print(f'Rezept: {selected_recipe['name']}')
                    print(f'Portionen: {selected_recipe['portions']}')

                    print("\nZutaten:")

                    for ingredients in selected_recipe['ingredients']:
                        print(f' - {ingredients['name']}: {ingredients['amount']:.0f} {ingredients['unit']}')
                    
                    if selected_recipe['allergies'] == []:
                        print('\nAllergien: keine erfasst')
                    else: print(f'\nAllergien: {selected_recipe['allergies']}')
                    
                    if selected_recipe['favorite'] == False:
                        print('Favorit: nein\n')
                    else: print('Favorit: ja\n')
                    
                    print('=== VIEL FREUDE BEIM KOCHEN ! ===\n')
                    break
            
                # Fehleingaben
                else: print(' \n--- kein Rezept gefunden --- \n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gebe die Nummer des gewünschten Rezepts ein)') # falsche Zahl
            else: print ('\n--- kein Rezept gefunden ---\n[ERROR] Eingabe ungültig ! (siehe unter "Deine Rezepte" und gib eine gültige ZAHL ein)') # Buchstaben statt Zahl

        # Schleife nach Menüauswahl
        while True:
            move = input('wähle "R" für Rezeptliste oder "H" für Hauptmenü: ').strip().lower()

            # Schleife nach ungültiger Eingabe
            while move != "r" and move != "h":
                move = input('\n[ERROR] Eingabe ungültig ! (gib "r" oder "h" ein): ').lower().strip()

            if move == "r":
                break
            elif move == "h":
                return

# US03 codiert soweit ready - nur noch Doku + "clean-terminal" Funktion noch offen falls noch Zeit bleibt
