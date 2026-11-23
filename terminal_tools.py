import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def back_to_menu():
    input("\nDrücke Enter, um zum Hauptmenü zurückzukehren.")

def handle_menu_return(choice):
    if choice not in ("1", "2", "3", "4", "5"):
        back_to_menu()