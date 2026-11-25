import importlib.util
import subprocess
import sys

def install_dependencies():
    if importlib.util.find_spec("reportlab") is not None:
        return

    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "reportlab"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        print("ReportLab wurde erfolgreich installiert.")

    except subprocess.CalledProcessError:
        print("Fehler: ReportLab konnte nicht installiert werden.")
        print("Bitte überprüfe deine Internetverbindung.")
        sys.exit(1)