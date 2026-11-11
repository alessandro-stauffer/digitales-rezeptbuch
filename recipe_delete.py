# Zugriff zu vorhandenen Rezepten 
import json


# weiteres Vorgehen nachdem Rezept ausgewählt

 #def recipe_delete(decision,input):
decision = input("Bist du dir ganz sicher, dass du das Rezept löschen möchtest? ").strip().lower()
if decision == "j":
    print("Alles klar, das Rezept wurde erfolgreich gelöscht !")

elif decision == "n":
    print("Puuh, Glück gehabt, nichts ist gelöscht oder verloren :)")

else: print('Oh, tut mir Leid, ich habe deine Eingabe nicht verstanden - antworte am besten mit "j" oder "n" ;) ')




from storage import load_recipes # Funktion Rezepte einfügen

def recipe_delete(recipes):
    recipes = def load_recipes() # Rezepte suchen
    if not recipes:
        return
        print("Keine Rezepte gefunden")

    rezept_ID = input ("Welches Rezept möchtest du löschen?")

        