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