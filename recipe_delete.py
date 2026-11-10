# Zugriff zu vorhandenen Rezepten 
import json


# weiteres Vorgehen nachdem Rezept ausgewählt

def recipe_delete(decision):
    decision = input("Bist du dir ganz sicher, dass du das Rezept löschen möchtest? ").strip().lower()
        if decision == "j":
            print("Alles klar, das Rezept wurde erfolgreich gelöscht !")

        elif decision == "n":
            print("Puuh, Glück gehabt, nichts ist gelöscht oder verloren :)")

        else: print('Oh, tut mir Leid, ich habe deine Eingabe nicht verstanden - antworte am besten mit "j" oder "n" ;) ')


    