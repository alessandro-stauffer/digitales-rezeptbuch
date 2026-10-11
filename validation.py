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
