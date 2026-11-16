# import json überflüssig - gelöscht !

# Tool: Rezepte laden
from storage import load_recipes

# Funktion Rezepte anzeigen
def show_recipes():
    recipes = load_recipes()

    # Status Rezeptbuch ist leer
    if not recipes:
        print('\n--- keine Rezepte vorhanden ---\n')
        return

    # Schleife zurück
    while True:

        # vorhandene Rezepte
        print('\n=== Deine Rezepte ===')

        # i = Startpunkt
        for i, recipe in enumerate (recipes):

            # +1 wegen Nummerierung ab 0
            print(f'{i+1}. {recipe["name"]}')

        # Rezept öffnen
        number = input('\nWähle Rezept-Nr.: ')

        # Prüfung int
        if number.isdigit():

            # Umwandlung Zahl
            number = int(number)

            # Prüfung Rezeptliste Anz.
            if 1 <= number <= len(recipes):
                selected_recipe = recipes[number - 1]

                # Detailansicht
                print('\n --- Rezeptdetails ---\n')

                print(f'Rezept: {selected_recipe['name']}')
                print(f'Portionen: {selected_recipe['portions']}')

                print("\nZutaten:")

                for ingredients in selected_recipe['ingredients']:
                    print(f' - {ingredients['name']}: {ingredients['amount']} {ingredients['unit']}')
                
                if selected_recipe['allergies'] == []:
                    print('\nAllergien: keine erfasst')
                else: print(f'\nAllergien: {selected_recipe['allergies']}')
                
                if selected_recipe['favorite'] == False:
                    print('Favorit: nein\n')
                else: print('Favorit: ja\n')
                
                print('*** VIEL FREUDE BEIM KOCHEN ! ***\n')
            
            # Fehleingaben
            else: print(' \n--- kein Rezept gefunden --- \n(Eingabe ungültig ! Siehe unter "Deine Rezepte" und gebe die Nummer des gewünschten Rezepts ein)\n') # falsche Zahl
        else: print ('\n--- kein Rezept gefunden ---\n(Eingabe ungültig ! Siehe unter "Deine Rezepte" und gib eine gültige ZAHL ein)\n') # Buchstaben statt Zahl

    # To do: Loop einbauen !
    #    while True:
    #    move = input('Wähle "r" für zurück zur Rezeptliste oder "h" für zurück ins Hauptmenü: ').strip().lower()
    #    if move == "r":
    #        continue
    #    elif move == "h":
    #        break
    #    elif: print('Eingabe ungültig ! Gib "r" oder "h" ein')



            










# Wähle h für zurück zum Hauptmenü 

# To do: Terminal löschen nach gültiger Eingabe?

# Loop ? main.py oder display.py ?
# Ansicht nochmals anpassen - aber zuerst gemeinsamer Test am Mo

show_recipes()