import sys
import subprocess
import importlib.util

def install_dependencies():
    if importlib.util.find_spec("reportlab") is None:
        print("Reportlab ist nicht installiert. Installation startet...")

        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "reportlab"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("Reportlab wurde erfolgreich installiert.")