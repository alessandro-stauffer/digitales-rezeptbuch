import math

def validate_text(recipe_name):
    bereinigter_text = recipe_name.strip()
    if bereinigter_text == "":
        return False
    else:
        return True

def validate_portions(portions_text):
    try:
        portions = int(portions_text)
        if portions > 0:
            return portions
        else:
            return None
    except ValueError:
        return None

def validate_amount(amount_text):
    try:
        amount = float(amount_text)
        if amount > 0 and math.isfinite(amount):
            return amount
        else:
            return None
    except ValueError:
        return None

def validate_unit(unit_text):
    allowed_units = ["g", "ml", "Stück"]
    if unit_text in allowed_units:
        return True
    else:
        return False

def validate_yes_no(answer_text):
    if answer_text == "j":
        return True
    elif answer_text == "n":
        return False
    else:
        return None

def validate_import_recipe(recipe):
    if (
        isinstance(recipe, dict)
        and "name" in recipe
        and "portions" in recipe
        and "ingredients" in recipe
    ):
        name = recipe["name"]
        portions = recipe["portions"]
        ingredients = recipe["ingredients"]
        if (
            isinstance(name, str)
            and validate_text(name)
            and type(portions) is int
            and portions > 0
            and isinstance(ingredients, list)
            and len(ingredients) > 0
        ):
            for ingredient in ingredients:
                if not isinstance(ingredient, dict):
                    return False
                if (
                    "name" not in ingredient
                    or "amount" not in ingredient
                    or "unit" not in ingredient
                ):
                    return False
                ingredient_name = ingredient["name"]
                if (
                    not isinstance(ingredient_name, str)
                    or not validate_text(ingredient_name)
                ):
                    return False
                amount = ingredient["amount"]
                if type(amount) not in (int, float):
                    return False
                if validate_amount(amount) is None:
                    return False
                unit = ingredient["unit"]
                if not validate_unit(unit):
                    return False
            return True
        else:
            return False
    else:
        return False