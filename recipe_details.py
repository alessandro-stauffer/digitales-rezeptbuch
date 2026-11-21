# Funktion Rezeptdetails auslagern

from recipe_tools import select_recipe

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





