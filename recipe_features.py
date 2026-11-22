from storage import load_recipes
from storage import save_recipes

allergies = ["Gluten", "Laktose", "Nüsse", "Eier", "Soja", "Sesam", "Krebstiere", "Weichtiere"]

def ask_recipe_allergies():
    list_allergies = []
 
    print("Gib an, welche Allergien von diesem Rezept betroffen sind:")
    number = 1
    for allergy in allergies:
        print(f"{number}: {allergy}")
        number += 1
 
    valid_input = [str(x) for x in range(1, len(allergies)+1)]
 
    while True: #while loop damit immer wieder nach Input gefragt wird. while loop wird beendet sobald etwas returned wird
        user_input = input("Allergie auswählen (1-8 oder fertig): ").strip()
        if user_input.lower() == "fertig":
            return list_allergies
        elif user_input == "":
            print("Bitte gib eine Nummer ein.")
        elif user_input not in valid_input:
            print(f"Ungültige Eingabe. Bitte eine Nummer zwischen 1 und {len(allergies)} eingeben.")
        else:
            allergy = allergies[int(user_input) - 1]
            if allergy in list_allergies:
                print(f"{allergy} ist bereits in der Liste vorhanden.")
            else:
                list_allergies.append(allergy)
                print(f"{allergy} wurde hinzugefügt.")

def input_ingredients():
    stored_ingredients = []

    while True:
        user_input = input("Gib die Zutaten ein, nach welchen du suchst. Wenn du fertig bist, bitte mit 'fertig' antworten: ")
        user_input = user_input.strip().lower()
        if user_input == "fertig":
            if len(stored_ingredients) > 0:
                return stored_ingredients
            print("Bitte gib mind. eine Zutat ein. ") #wenn user fertig schreibt, obwohl noch keine Zutat der Liste beigefügt wurde
        elif user_input == "":
            print("Bitte gib eine Zutat mit mind. einen Buchstaben ein. ")
        else:
            stored_ingredients.append(user_input)
            print(f"{user_input.capitalize()} wurde hinzugefügt.")


def ingredient_filter():

    print('\n=== Nach Zutaten filtern ===')
    print()
    recipes = load_recipes()
    result = input_ingredients()
    filtered_recipe = []
    for recipe in recipes:
        recipe_ingredients = recipe["ingredients"]
        ingredients_names = []
        for single_ingredient in recipe_ingredients:
            ingredients_names.append(single_ingredient["name"].lower())

        recipe_fits = True
        for ingredient in result:
            if ingredient not in ingredients_names:
                recipe_fits = False
                break

        if recipe_fits:
            filtered_recipe.append(recipe)

    print()

    if filtered_recipe == []:
        print("Es wurden keine Rezepte gefunden.")
    else:
        print(f"Das sind die Rezepte, die deinen Suchkriterien entsprechen: {', '.join([recipe['name'] for recipe in filtered_recipe])}")

    return filtered_recipe


def user_input1_favorites(): #checkt nur user input1. Wenn ungültig wird wieder gefragt mithilfe while loop
    recipes = load_recipes()
    all_ids = []
    for recipe in recipes:
        all_ids.append(recipe["id"])
    while True:
        user_input1 = input("Welches Rezept möchtest du bearbeiten? (Bitte ID angeben): ")
        if user_input1.isdigit() and int(user_input1) in all_ids:
            return user_input1
        print("Die ID existiert nicht. Bitte überprüfe sie und versuche es noch einmal. ")


def user_input2_favorites(): #checkt nur user input2. Wenn ungültig wird wieder gefragt mithilfe while loop
    while True:
        print('\n=== Favoriten bearbeiten ===')
        print('\n1. Hinzufügen [H]' )
        print('2. Entfernen [E]')
        user_input2 = input("\nWähle anhand der Nummer was du machen möchtest: ")
        if user_input2.upper().strip() == "H" or user_input2.upper().strip() == "E":
            return user_input2
        print("Deine Eingabe ist ungültig. Bitte überprüfe sie und versuche es noch einmal: ")


def get_favorites():
    recipes = load_recipes()
    favorite_recipes = []
    for recipe in recipes:
        if recipe["favorite"] == True:
            favorite_recipes.append(recipe)

    if favorite_recipes == []:
        print("Du hast keine Favoriten gespeichert. ")
    else:
        print(f"Diese Rezepte sind in deinen Favoriten: {', '.join([recipe['name'] for recipe in favorite_recipes])}")

    return favorite_recipes


def edit_favorites():
    recipes = load_recipes()
    print('\n=== Favoriten ===')
    print('\n1. Favoriten anzeigen' )
    print('2. Favoriten bearbeiten')
    show_favorites = input("\nWähle anhand der Nummer was du machen möchtest: ")
    if show_favorites == "2" or show_favorites == "2.":
        print() #um einen Abstand vor den Rezepten einzufügen
        for recipe in recipes:
            print(f"Rezept: {recipe['name']}; ID: {recipe['id']}; Favorites: {recipe['favorite']}")
        print() #um einen Abstand vor den Rezepten einzufügen
        user_input1 = user_input1_favorites()
        user_input2 = user_input2_favorites()
        for recipe in recipes:
            if user_input1 == str(recipe["id"]):
                if user_input2.upper().strip() == "H":
                    recipe["favorite"] = True
                    print(f"Das Rezept für {recipe['name']} wurde zu den Favoriten hinzugefügt")
                elif user_input2.upper().strip() == "E":
                    recipe["favorite"] = False
                    print(f"Das Rezept für {recipe['name']} wurde von den Favoriten entfernt")
        save_recipes(recipes)
    else:
        print() #um einen Abstand vor den Rezepten einzufügen
        get_favorites()


def user_input_allergies():
    list_allergies = []
    valid_input = [str(x) for x in range(1, len(allergies)+1)]

    while True:
        user_input = input("Wähle anhand der Nummer nach welchen Allergien du filtern möchtest (1-8 oder fertig): ")
        if user_input.lower().strip() == "fertig":
            if len(list_allergies) > 0:
                return list_allergies
            print("Bitte gib mind. eine Allergie ein. ") #wenn user fertig schreibt, obwohl noch keine Zutat der Liste beigefügt wurde
        elif user_input.strip() == "": 
            print("Bitte gib eine Numemr ein. ")
        elif user_input.strip() not in valid_input:
            print(f"Ungültige Eingabe. Bitte gib eine Nummer zwischen 1 und {len(allergies)} oder 'fertig' ein.")
        else:
            allergy = allergies[int(user_input) - 1]
            if allergy in list_allergies:
                print(f"{allergy} ist bereits in der Liste vorhanden.")
            else:
                list_allergies.append(allergy)
                print(f"{allergy} wurde hinzugefügt.")


def allergies_filter():
    
    print('\n=== Allergien ===')
    number = 1
    print()
    for allergy in allergies:
        print(f"{number}: {allergy}")
        number += 1

    print()
    input_allergies = user_input_allergies() #Liste mit eingegebenen Allergien
    recipes = load_recipes()

    list_filtered_recipes = []
    for recipe in recipes:
        recipe_fits = True
        for allergy in input_allergies:
            if allergy in recipe["allergies"]:
                recipe_fits = False

        if recipe_fits == True:
            list_filtered_recipes.append(recipe) #only appends recipes which do not have the listed allergies in them

    if list_filtered_recipes == []:
        print("\nEs wurden keine Rezepte ohne diese Allergien gefunden.")
    else:
        print(f"\nDiese Rezepte enthalten keine deiner angegebenen Allergien: {', '.join([recipe['name'] for recipe in list_filtered_recipes])}")
        
    return list_filtered_recipes 
  

# def recipe_filter():
#     recipe_allergies = allergies_filter()
#     ingredient_recipes = ingredient_filter()

#     filtered_recipes = []
#     for recipe in ingredient_recipes:
#         if recipe in recipe_allergies:
#             filtered_recipes.append(recipe)

#     if filtered_recipes == []:
#         print("Es wurden keine Rezepte gefunden.")
#     else:
#         print(f"Das sind deine gefilterten Rezepte: {', '.join([recipe['name'] for recipe in filtered_recipes])}")
       
#     return filtered_recipes