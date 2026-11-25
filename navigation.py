import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[3J", end="", flush=True)

def choose_next_action(options):
    while True:
        print("\n=== Was möchtest du als Nächstes tun? ===")

        for number, text in options.items():
            print(f"{number}. {text}")

        choice = input("\nWähle eine Option: ").strip()

        if choice in options:
            return choice

        print("Ungültige Eingabe. Bitte versuche es erneut.")