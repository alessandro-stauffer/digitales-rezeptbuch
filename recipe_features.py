from storage import load_recipes
from storage import save_recipes

allergies = ["Gluten", "Laktose", "Nüsse", "Eier", "Soja", "Sesam", "Krebstiere", "Weichtiere"]

def input_ingredients():
    stored_ingredients = []

    while True:
        user_input = input("Nach welchen Zutaten suchst du? Wenn du fertig bist, bitte mit 'fertig' antworten.")
        user_input = user_input.strip().lower()
        if user_input == "fertig":
            if len(stored_ingredients) > 0:
                return stored_ingredients
            print("Bitte gib mind. eine Zutat ein.") #wenn user fertig schreibt, obwohl noch keine Zutat der Liste beigefügt wurde
        elif user_input == "":
            print("Bitte gib eine Zutat mit mind. einen Buchstaben ein.")
        else:
            stored_ingredients.append(user_input)


def recipe_filter():
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

    if filtered_recipe == []:
        print("Es wurden keine Rezepte gefunden.")

    return filtered_recipe


def get_favorites():
    recipes = load_recipes()
    favorite_recipes = []
    for recipe in recipes:
        if recipe["favorite"] == True:
            favorite_recipes.append(recipe)

    if favorite_recipes == []:
        print("Du hast keine Favoriten gespeichert.")
    return favorite_recipes


def edit_favorites():
    recipes = load_recipes()
    for recipe in recipes:
        print(f"Rezept: {recipe['name']}; ID: {recipe['id']}")
    user_input1 = user_input1_favorites(recipes)
    user_input2 = user_input2_favorites()
    for recipe in recipes:
        if user_input1 == str(recipe["id"]):
            if user_input2.lower().strip() == "hinzufügen":
                recipe["favorite"] = True
                print(f"Das Rezept für {recipe['name']} wurde zu den Favoriten hinzugefügt")
            elif user_input2.lower().strip() == "entfernen":
                recipe["favorite"] = False
                print(f"Das Rezept für {recipe['name']} wurde von den Favoriten entfernt")

    save_recipes(recipes)


def user_input2_favorites(): #checkt nur user input2. Wenn ungültig wird wieder gefragt mithilfe while loop
    while True:
        user_input2 = input("Möchtest du das Rezept von den Favoriten entfernen oder zu den Favoriten hinzufügen? (Bitte mit 'entfernen' oder 'hinzufügen' antworten.)")
        if user_input2.lower().strip() == "hinzufügen" or user_input2.lower().strip() == "entfernen":
            return user_input2
        print("Deine Eingabe ist ungültig. Bitte überprüfe sie und versuche es noch einmal.")


def user_input1_favorites(recipes): #checkt nur user input1. Wenn ungültig wird wieder gefragt mithilfe while loop
    all_ids = []
    for recipe in recipes:
        all_ids.append(recipe["id"])
    while True:
        user_input1 = input("Welches Rezept möchtest du bearbeiten? (Bitte ID angeben)")
        if user_input1.isdigit() and int(user_input1) in all_ids:
            return user_input1
        print("Die ID existiert nicht. Bitte überprüfe sie und versuche es noch einmal.")


def user_input1_allergies():
    list_allergies = []

    while True:
        user_input1 = input("Welche Allergien möchtest du hinzufügen oder entfernen? Wenn du fertig bist, bitte mit 'fertig' antworten.")
        if user_input1.lower().strip() in [x.lower() for x in allergies] and user_input1.lower().strip().capitalize() not in list_allergies:
            list_allergies.append(user_input1.lower().strip().capitalize())
        elif user_input1.lower().strip() == "fertig":
            if len(list_allergies) > 0:
                return list_allergies
            print("Bitte gib mind. eine Allergie ein.") #wenn user fertig schreibt, obwohl noch keine Zutat der Liste beigefügt wurde
        elif user_input1.strip() == "": 
            print("Bitte gib eine Allergie mit mind. einem Buchstaben ein.")
        elif user_input1.lower().strip().capitalize() in list_allergies:
            print("Die Allergie ist bereits in der Liste vorhanden.")
        else:
            print("Die Allergie ist nicht in der Liste enthalten. Bitte überprüfe sie und versuche es noch einmal.")


def user_input2_allergies(): #checkt nur user input2. Wenn ungültig wird wieder gefragt mithilfe while loop
    while True:
        user_input2 = input("Möchtest du die Allergie(n) entfernen oder hinzufügen? (Bitte mit 'entfernen' oder 'hinzufügen' antworten.)")
        if user_input2.lower().strip() == "hinzufügen" or user_input2.lower().strip() == "entfernen":
            return user_input2
        print("Deine Eingabe ist ungültig. Bitte überprüfe sie und versuche es noch einmal.")


def edit_allergies():
    recipes = load_recipes()
    for recipe in recipes:
        print(f"Rezept: {recipe['name']}; ID: {recipe['id']}^; Allergien: {recipe['allergies']}")
    user_input1 = user_input1_allergies()
    user_input2 = user_input2_allergies()
    for recipe in recipes:
        if user_input2 == "hinzufügen":
            for allergy in user_input1:
                recipe["allergies"].append(allergy) #wir haben schon bei user_input2_allergies gecheckt ob 
        elif user_input2 == "entfernen":
            for allergy in user_input1:  
