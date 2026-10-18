# Digitales Rezeptbuch – Programmdesign

## 1. Projektübersicht

Das Projekt ist eine lokale Python-Kommandozeilenanwendung (CLI), mit der Benutzer Rezepte erfassen, speichern, anzeigen, bearbeiten und verwalten können. Die Anwendung wird von vier Gruppenmitgliedern gemeinsam entwickelt. Die einzelnen Funktionen werden auf mehrere Python-Module verteilt.

**Dokumentationsstand:** Die grundlegende Rezepterfassung (US01) und die dazu benötigten Eingabeprüfungen (US09) sind implementiert und manuell getestet. Weitere User Storys und die Integration in das gemeinsame Hauptmenü sind noch in Entwicklung. Die nachfolgend beschriebenen Funktionen werden als *implementiert* oder *geplant* gekennzeichnet.

## 2. Datenmodell

Alle Rezepte werden während der Programmausführung in einer Liste (`list`) verwaltet. Jedes Rezept ist ein Dictionary (`dict`). Die Liste wird zur dauerhaften Speicherung als JSON-Datei geschrieben.

### 2.1 Rezept

| Feld | Datentyp | Beschreibung |
|---|---|---|
| `id` | `int` | Innerhalb der aktuellen Rezeptliste eindeutige Identifikationsnummer |
| `name` | `str` | Name des Rezepts; darf nicht leer sein |
| `portions` | `int` | Anzahl Portionen, grösser als 0 |
| `ingredients` | `list` | Liste von mindestens einem Zutaten-Dictionary |
| `favorite` | `bool` | Kennzeichnung als Favorit |
| `allergies` | `list` | Liste zugeordneter Allergietypen |

Neue Rezepte erhalten standardmässig `favorite = False` und eine leere Allergienliste `[]`. Favoriten und Allergien werden in anderen User Storys weiterbearbeitet.

Beispiel eines neu erfassten Rezepts:

```python
{
    "id": 1,
    "name": "Pfannkuchen",
    "portions": 2,
    "ingredients": [
        {"name": "Mehl", "amount": 250.0, "unit": "g"},
        {"name": "Milch", "amount": 200.0, "unit": "ml"}
    ],
    "favorite": False,
    "allergies": []
}
```

### 2.2 Zutat

Jede Zutat wird ebenfalls als Dictionary dargestellt.

| Feld | Datentyp | Beschreibung |
|---|---|---|
| `name` | `str` | Name der Zutat; darf nicht leer sein |
| `amount` | `float` | Endliche, positive Menge, grösser als 0 |
| `unit` | `str` | Einheit der Zutat |

Zulässige Einheiten in der aktuellen Umsetzung: `g`, `ml`, `Stück`. Die Eingabe wird derzeit auf diese exakten Schreibweisen geprüft.

### 2.3 Identifikation

Jedes Rezept erhält eine eindeutige ID. Die ID wird beim Bearbeiten eines Rezepts nicht verändert. Die ID muss innerhalb der aktuell gespeicherten Rezepte eindeutig sein.

Beim Erstellen eines neuen Rezepts wird die höchste vorhandene ID um 1 erhöht. Falls keine Rezepte vorhanden sind, beginnt die Nummerierung bei 1. Bei dieser Regel können gelöschte IDs nur dann erneut vergeben werden, wenn sie oberhalb der höchsten aktuell verbliebenen ID liegen. Eine lückenlose Nummerierung ist nicht erforderlich.

## 3. Datenspeicherung

Die dauerhafte Speicherung erfolgt lokal in der JSON-Datei `data/recipes.json`.

- `save_recipes(recipes)` in `storage.py` schreibt die gesamte Rezeptliste mit `json.dump()`.
- `load_recipes()` in `storage.py` lädt sie mit `json.load()`.
- Die Datei wird mit UTF-8 verarbeitet; `ensure_ascii=False` erhält Umlaute lesbar, `indent=4` formatiert die Ausgabe.
- Beim Speichern wird der Dateimodus `"w"` verwendet. Deshalb müssen vor dem Hinzufügen eines Rezepts die bisherigen Rezepte geladen werden, damit diese nicht überschrieben werden.
- Existiert die JSON-Datei nicht, gibt `load_recipes()` eine leere Liste `[]` zurück.
- Enthält die Datei ungültiges JSON, zeigt `load_recipes()` eine Fehlermeldung und gibt den `json.JSONDecodeError` mit `raise` weiter. Dadurch wird der normale Ablauf vor dem Speichern unterbrochen.

**Stand der Umsetzung:** Lesen, Schreiben, erneutes Laden nach Programmneustart sowie die beiden genannten Fehlerfälle wurden manuell getestet. Weitere Fehlerfälle, insbesondere fehlende Schreibrechte, sind noch nicht gesondert behandelt. Die verwendeten relativen Pfade setzen derzeit voraus, dass das Programm aus dem Projektverzeichnis gestartet wird.

## 4. Grundprinzipien

- Eingabe, Verarbeitung und Ausgabe werden möglichst getrennt.
- Eine Funktion soll eine klar definierte Aufgabe erfüllen.
- Die Module verwenden das gemeinsame Datenmodell.
- Ungültige Benutzereingaben sollen keinen Programmabbruch verursachen, sondern erneut abgefragt werden.
- Rezeptänderungen werden dauerhaft gespeichert.
- Beschädigte gespeicherte Daten dürfen nicht stillschweigend überschrieben werden.
- Gemeinsame Funktionen sollen durch andere Module wiederverwendbar sein.

## 5. Getroffene und offene Entscheidungen

### 5.1 Getroffene Entscheidungen

- Ein Rezept muss mindestens eine Zutat enthalten.
- Die aktuell erlaubten Einheiten sind `g`, `ml` und `Stück`.
- Rezept-IDs werden nach der Regel *höchste vorhandene ID + 1* vergeben; bei leerer Liste beginnt die Zählung bei 1.
- Neue Rezepte erhalten `favorite = False` und `allergies = []`.
- Eine fehlende `data/recipes.json` führt beim Laden zu einer leeren Rezeptliste.
- Eine JSON-Datei mit ungültigem Inhalt verursacht eine Fehlermeldung und einen Abbruch des aktuellen Ablaufs, damit sie nicht überschrieben wird.
- Die dauerhafte Datenspeicherung erfolgt über `storage.py`.

### 5.2 Noch offene Entscheidungen

- Welche Allergietypen stehen zur Auswahl?
- Welches konkrete Importformat verwendet US02? (Noch nicht festgelegt.)
- Benötigt das Rezept zusätzlich ein Feld für Freitext/Kochanweisungen? (Noch nicht entschieden.)
- Wie sollen Schreibfehler bei der Dateispeicherung und fehlerhafte Datenstrukturen in gültigem JSON behandelt werden?
- Sollen die Einheiten- und Ja/Nein-Eingaben später auch alternative Schreibweisen erlauben (z. B. `stück`, `J`)?

## 6. Modulstruktur

Das Programm ist in mehrere Python-Module aufgeteilt. Jedes Modul übernimmt einen möglichst klar abgegrenzten Aufgabenbereich.

### 6.1 Modulübersicht und Verantwortlichkeiten

| Modul | Aufgabe | User Story / Bezug | Verantwortlich |
|---|---|---|---|
| `main.py` | Programmstart und Ablaufsteuerung; bisher `create_recipe()`, später Hauptmenü | US01 / US10 | US01-Integration: Alessandro; Hauptmenü: Agshayan |
| `recipe_input.py` | Neue Rezepte und Zutaten interaktiv erfassen | US01 | Alessandro |
| `validation.py` | Benutzereingaben überprüfen | US09 | Alessandro |
| `storage.py` | Rezeptdaten laden und speichern; Importfunktion geplant | Gemeinsame Datenspeicherung / US02 | Alessandro / Team |
| `recipe_management.py` | IDs für neue Rezepte vergeben; Anzeigen, Bearbeiten, Löschen geplant | US01 / US03–US05 | ID-Vergabe: Alessandro; weitere Verwaltung: Jennifer |
| `recipe_tools.py` | Zutatenmengen skalieren und Einkaufslisten erstellen | US06, US07 | Agshayan |
| `recipe_features.py` | Rezepte filtern, Favoriten und Allergien verwalten | US08, US11, US12 | Mai |

### 6.2 Zusammenarbeit der Module

- `main.py` koordiniert die Funktionen und ruft für US01 die Eingabe, ID-Vergabe und Speicherung auf.
- `recipe_input.py` ruft die passenden Funktionen aus `validation.py` auf.
- `recipe_management.py` ermittelt die nächste ID anhand bereits vorhandener Rezepte.
- `storage.py` liest und schreibt die gemeinsame JSON-Rezeptliste.
- Andere Module erhalten benötigte Daten über Parameter und Rückgabewerte.
- Ein gemeinsames Hauptmenü ist geplant und noch nicht Teil der aktuell getesteten US01-Funktion.

### 6.3 Entwicklungsprinzipien

- Jedes Modul enthält logisch zusammengehörige Funktionen.
- Jede Funktion soll möglichst nur eine Aufgabe erfüllen.
- Eingabe, Verarbeitung und Ausgabe sollen soweit sinnvoll getrennt werden.
- Die gesamte Gruppe verwendet dasselbe Datenmodell.
- Jedes Gruppenmitglied entwickelt seine zugeteilten User Storys selbstständig.
- Änderungen werden über eigene Git-Branches, Commits und Pull Requests dokumentiert.
- Die Modulverantwortlichkeiten und Schnittstellen werden bei der Integration innerhalb der Gruppe abgestimmt.

## 7. Function Tree

Die Anwendung wird in kleine, wiederverwendbare Funktionen unterteilt. Die Übersicht unterscheidet die bereits implementierten Funktionen von geplanten Teilen.

### 7.1 Implementierte Funktionen (US01 und verwendete US09-Funktionen)

| Modul | Funktion | Aufgabe |
|---|---|---|
| `main.py` | `create_recipe()` | Gesamten Ablauf von Laden bis Speichern koordinieren |
| `recipe_input.py` | `ask_recipe()` | Rezeptdaten ohne ID erfassen und Dictionary erstellen |
| `recipe_input.py` | `ask_recipe_name()` | Gültigen Rezeptnamen abfragen |
| `recipe_input.py` | `ask_portions()` | Gültige Portionszahl abfragen |
| `recipe_input.py` | `ask_ingredients()` | Eine oder mehrere Zutaten erfassen |
| `recipe_input.py` | `ask_ingredient()` | Ein Zutaten-Dictionary erstellen |
| `recipe_input.py` | `ask_ingredient_name()` | Gültigen Zutatennamen abfragen |
| `recipe_input.py` | `ask_ingredient_amount()` | Gültige Menge abfragen |
| `recipe_input.py` | `ask_ingredient_unit()` | Gültige Einheit abfragen |
| `validation.py` | `validate_text()` | Nicht leeren Text erkennen (`bool`) |
| `validation.py` | `validate_portions()` | Positive Ganzzahl oder `None` zurückgeben |
| `validation.py` | `validate_amount()` | Positive, endliche Dezimalzahl oder `None` zurückgeben |
| `validation.py` | `validate_unit()` | Erlaubte Einheit prüfen (`bool`) |
| `validation.py` | `validate_yes_no()` | `j` → `True`, `n` → `False`, sonst `None` |
| `recipe_management.py` | `generate_next_id(recipes)` | Nächste Rezept-ID berechnen |
| `recipe_management.py` | `add_recipe_id(recipe, recipes)` | ID zum neuen Rezept-Dictionary hinzufügen |
| `storage.py` | `load_recipes()` | Rezeptliste aus JSON laden |
| `storage.py` | `save_recipes(recipes)` | Rezeptliste als JSON speichern |

### 7.2 Geplante weitere Funktionen

| Modul | Geplante Funktionen / Aufgaben |
|---|---|
| `main.py` | `main()`, `show_menu()`, `process_choice()` – gemeinsames Hauptmenü und Steuerung |
| `storage.py` | Importfunktion für US02; genauer Name und Format noch offen |
| `recipe_management.py` | `show_recipes()`, `edit_recipe()`, `delete_recipe()` |
| `recipe_tools.py` | `scale_recipe()`, `create_shopping_list()` |
| `recipe_features.py` | `filter_recipes()`, `manage_favorites()`, `manage_allergies()` |

Die geplanten Funktionsnamen bleiben vorläufig, bis die jeweiligen User Storys umgesetzt und im Team integriert sind.

### 7.3 Grundsätze

- Funktionen werden möglichst für genau eine Aufgabe eingesetzt.
- Gemeinsam benötigte Funktionen werden wiederverwendet.
- Die Module tauschen Daten über Parameter und Rückgabewerte aus.
- `main.py` koordiniert den Ablauf, während andere Module Eingabe, Validierung, Verwaltung und Speicherung übernehmen.

## 8. Main Decision and Control Flow

### 8.1 Programmstart

**Geplant für die Gesamtanwendung:**

1. Das Programm wird gestartet.
2. Bereits gespeicherte Rezepte werden aus der JSON-Datei geladen.
3. Das Hauptmenü wird angezeigt.

**Aktuell implementiert:** `main.py` definiert die Funktion `create_recipe()`. Die Rezepterfassung startet erst, wenn diese Funktion aufgerufen wird; das spätere Hauptmenü ist noch nicht integriert.

### 8.2 Menüsteuerung (geplant)

1. Der Benutzer gibt eine Menüauswahl ein.
2. Die Eingabe wird geprüft.
3. Bei ungültiger Auswahl erscheint eine Fehlermeldung.
4. Bei gültiger Auswahl wird die entsprechende Funktion ausgeführt.
5. Nach Abschluss einer Funktion wird das Hauptmenü erneut angezeigt.
6. Dieser Ablauf wiederholt sich, bis der Benutzer das Programm beendet.

### 8.3 Datenänderungen

- Beim Erfassen, Bearbeiten oder Löschen von Rezepten werden Rezeptdaten geändert.
- Änderungen an Favoriten und Allergien sollen ebenfalls gespeichert werden.
- Die Daten werden nach erfolgreichen Änderungen in die JSON-Datei geschrieben.
- Die geplante Skalierung von Zutaten soll das ursprüngliche Rezept nicht verändern.

### 8.4 Kontrollstrukturen

- `if`, `elif`, `else`: Entscheidungen und Eingabeprüfung
- `while`: Wiederholung ungültiger Eingaben und mehrerer Zutaten; später Hauptmenü
- `for`: Durchlaufen von Rezepten bei der Ermittlung der höchsten ID und weitere Listenverarbeitung
- `try`, `except`, `raise`: Behandlung von Eingabe- und Dateifehlern

### 8.5 Fehlerbehandlung

Ungültige Benutzereingaben werden verständlich gemeldet und erneut abgefragt. Zahlen werden mit `try`/`except ValueError` umgewandelt. Beim Laden der JSON-Datei gibt eine fehlende Datei `[]` zurück. Eine beschädigte JSON-Datei führt dagegen zu einer Fehlermeldung und Weitergabe des Fehlers, um unbeabsichtigtes Überschreiben zu vermeiden. Fehler beim Schreiben der Datei sind noch nicht gesondert behandelt.

### 8.6 Control Flow – US01 Rezeptnamenvalidierung (implementiert)

**Ziel:** Sicherstellen, dass der Benutzer einen gültigen, nicht leeren Rezeptnamen eingibt.

**Zuständige Module:**

- `recipe_input.py`: `ask_recipe_name()` – Benutzereingabe und Wiederholung
- `validation.py`: `validate_text()` – Überprüfung des Textes

**Ablauf:**

1. `ask_recipe_name()` fordert den Benutzer zur Eingabe eines Rezeptnamens auf.
2. Der eingegebene String wird an `validate_text()` übergeben.
3. `validate_text()` prüft mithilfe von `strip()`, ob der Text nur aus Leerzeichen besteht oder leer ist.
4. Bei ungültigem Text gibt `validate_text()` `False` zurück. Es erscheint eine Fehlermeldung, und die Eingabe wird mit `while` wiederholt.
5. Bei gültigem Text gibt `validate_text()` `True` zurück. Die Schleife endet, und `ask_recipe_name()` gibt den eingegebenen Rezeptnamen zurück.
6. Die Rezepterfassung fährt mit der Portionszahl fort.

**Verwendete Python-Konzepte:** `input()`, `str`, `strip()`, `if`/`else`, `while`, `return`.

| Eingabe an `validate_text()` | Rückgabewert |
|---|---|
| `"Spaghetti Napoli"` | `True` |
| `"   "` | `False` |
| `""` | `False` |
| `"Risotto"` | `True` |

**Architekturentscheidung:** `validate_text()` validiert nur den übergebenen Wert. Die Funktion fordert keine Eingabe an und zeigt keine Meldung. Die aktuelle Eingabefunktion gibt den ursprünglich eingegebenen String zurück; sie entfernt Leerzeichen nicht dauerhaft.

### 8.7 Control Flow – US01 Portionsvalidierung (implementiert)

**Ziel:** Eine positive Ganzzahl für die Portionen erfassen.

**Zuständige Module:**

- `recipe_input.py`: `ask_portions()`
- `validation.py`: `validate_portions()`

**Ablauf:**

1. `ask_portions()` fragt nach der Portionszahl.
2. `validate_portions()` versucht, die Eingabe mit `int()` umzuwandeln.
3. Bei `ValueError` oder einer Zahl kleiner oder gleich 0 wird `None` zurückgegeben.
4. Bei einer positiven Ganzzahl wird der Integer zurückgegeben.
5. Bei `None` erscheint eine Fehlermeldung und die Eingabe wird wiederholt.
6. Sobald die Eingabe gültig ist, gibt `ask_portions()` den Integer zurück.

**Verwendete Python-Konzepte:** `input()`, `int()`, `try`/`except ValueError`, `if`, `while`, `return`.

### 8.8 Control Flow – US01 Zutatenerfassung (implementiert)

**Ziel:** Der Benutzer erfasst eine oder mehrere Zutaten. Jede Zutat besitzt einen Namen, eine Menge und eine Einheit.

**Architekturentscheidungen:**

- Ein Rezept benötigt mindestens eine Zutat.
- Jede Zutat wird als Dictionary dargestellt; alle Zutaten werden in einer Liste gesammelt.
- Die zulässigen Einheiten sind `g`, `ml`, `Stück`.
- Ungültige Eingaben werden einzeln wiederholt, ohne zuvor gültige Angaben zu verlieren.

**Zuständige Module:** `recipe_input.py` für die Eingabe und `validation.py` für die Prüfung.

#### 8.8.1 Einzelne Zutat erfassen

**Implementierte Funktion:** `ask_ingredient()`

1. `ask_ingredient_name()` fragt nach dem Zutatennamen; `validate_text()` überprüft die Eingabe.
2. `ask_ingredient_amount()` fragt nach der Menge; `validate_amount()` versucht die Umwandlung mit `float()` und akzeptiert nur endliche Werte grösser als 0. Dazu wird `math.isfinite()` verwendet.
3. `ask_ingredient_unit()` fragt nach der Einheit; `validate_unit()` prüft, ob sie in der Liste der zulässigen Einheiten enthalten ist.
4. Jede ungültige Teilangabe führt zu einer Fehlermeldung und einer erneuten Frage nach genau dieser Angabe.
5. `ask_ingredient()` erstellt und gibt ein Dictionary mit den Schlüsseln `name`, `amount` und `unit` zurück.

#### 8.8.2 Mehrere Zutaten erfassen

**Implementierte Funktion:** `ask_ingredients()`

1. Eine leere Zutatenliste `ingredients` wird erstellt.
2. Eine äussere `while`-Schleife erfasst mindestens eine Zutat mit `ask_ingredient()`.
3. Das Zutaten-Dictionary wird mit `ingredients.append(ingredient)` ergänzt.
4. Der Benutzer wird gefragt, ob er eine weitere Zutat hinzufügen möchte (`j`/`n`).
5. `validate_yes_no()` gibt bei `j` `True`, bei `n` `False`, sonst `None` zurück.
6. Eine innere `while`-Schleife wiederholt die Ja/Nein-Frage, solange das Ergebnis `None` ist.
7. Bei `True` wird eine weitere Zutat erfasst. Bei `False` endet die äussere Schleife.
8. Die vollständige Zutatenliste wird zurückgegeben.

#### 8.8.3 Rückgabewerte

| Funktion | Gültige Rückgabe | Ungültige Eingabe |
|---|---|---|
| `validate_text()` | `True` | `False` |
| `validate_amount()` | Positiver, endlicher `float` | `None` |
| `validate_unit()` | `True` | `False` |
| `validate_yes_no()` | `True` (`j`) oder `False` (`n`) | `None` |
| `ask_ingredient()` | Zutaten-Dictionary | Fragt intern erneut |
| `ask_ingredients()` | Liste mit mindestens einer Zutat | Fragt intern erneut |

#### 8.8.4 Verwendete Python-Konzepte

`input()`, `str`, `float`, `dict`, `list`, `append()`, `while`, `if`/`else`, `in`, `try`/`except ValueError`, `math.isfinite()`, `return`.

### 8.9 Control Flow – US01 Rezept erstellen und speichern (implementiert)

**Ziel:** Die gültig erfassten Rezeptdaten zu einem vollständigen Rezept zusammenführen, eine ID vergeben und die Rezeptliste dauerhaft speichern.

**Zuständige Module:**

- `main.py`: `create_recipe()` – Ablaufsteuerung
- `recipe_input.py`: `ask_recipe()` – Datenerfassung und Rezept-Dictionary ohne ID
- `recipe_management.py`: `generate_next_id()` und `add_recipe_id()` – ID-Vergabe
- `storage.py`: `load_recipes()` und `save_recipes()` – Dateiverarbeitung

#### 8.9.1 Rezept-Dictionary erstellen

1. `ask_recipe()` ruft nacheinander `ask_recipe_name()`, `ask_portions()` und `ask_ingredients()` auf.
2. Die Funktion erstellt ein Dictionary mit `name`, `portions` und `ingredients`.
3. Zusätzlich werden `favorite = False` und `allergies = []` gesetzt.
4. Das Dictionary wird **noch ohne ID** zurückgegeben.
5. `generate_next_id(recipes)` ermittelt mit einer `for`-Schleife und einem Vergleich die höchste vorhandene ID, erhöht diese um 1 und gibt bei leerer Liste 1 zurück.
6. `add_recipe_id(recipe, recipes)` ergänzt das Dictionary um den Schlüssel `id` und gibt es zurück.

#### 8.9.2 Vollständigen Ablauf ausführen und speichern

Die Funktion `create_recipe()` in `main.py` führt diese Schritte aus:

1. `load_recipes()` lädt die bestehende Rezeptliste.
2. `ask_recipe()` erfasst die Daten eines neuen Rezepts.
3. `add_recipe_id(recipe, recipes)` ergänzt die eindeutige ID.
4. `recipes.append(recipe)` fügt das Rezept zur Liste hinzu.
5. `save_recipes(recipes)` schreibt die aktualisierte Liste nach `data/recipes.json`.
6. `print(recipes)` gibt derzeit die vollständige Rezeptliste zu Test- und Kontrollzwecken aus.

Die Funktion wird derzeit gezielt aufgerufen; ihre Integration in das spätere Hauptmenü steht noch aus. Eine separate, benutzerfreundliche Erfolgsbestätigung ist noch nicht implementiert.

#### 8.9.3 Fehlerbehandlung und Datensicherheit

- `load_recipes()` behandelt `FileNotFoundError` mit einer leeren Rezeptliste `[]`.
- `load_recipes()` behandelt `json.JSONDecodeError` mit einer verständlichen Fehlermeldung und `raise`. Dadurch bricht der Ablauf ab, bevor `save_recipes()` ausgeführt wird.
- Die Funktion `save_recipes()` schreibt derzeit im Modus `"w"` und verwendet noch keine spezielle Behandlung von Schreibfehlern.
- Bei Fehlern während einer Speicherung darf das Programm künftig keinen Erfolg melden; diese zusätzliche Behandlung ist noch offen.

#### 8.9.4 ID-Vergabe

Die IDs werden nach der höchsten ID der aktuell vorhandenen Rezepte berechnet:

- Höchste vorhandene ID + 1
- Bei leerer Liste: ID 1

Die Umsetzung verwendet `highest_id = 0`, eine `for`-Schleife und einen `if`-Vergleich. Sie verwendet **nicht** die ursprünglich erwogene Funktion `max()`.

#### 8.9.5 Verwendete Python-Konzepte

`dict`, `list`, `append()`, `for`, `if`, `return`, Funktionsparameter und Rückgabewerte, Modul-Imports, `with open()`, `json.dump()`, `json.load()`, `try`/`except`, `raise`.

#### 8.9.6 Architekturprinzip

Die Eingabe, ID-Vergabe und dauerhafte Speicherung sind logisch getrennt. `main.py` koordiniert den Ablauf. `storage.py` stellt wiederverwendbare Funktionen zur Dateiverarbeitung bereit. `recipe_management.py` übernimmt die Berechnung und Zuweisung der ID.

### 8.10 Manuelle Tests – Stand US01

Folgende Verhaltensweisen wurden im Verlauf der Entwicklung manuell geprüft:

- Gültige und ungültige Rezeptnamen sowie Portionszahlen
- Gültige und ungültige Zutatenangaben einschliesslich negativer Mengen und `inf`
- Erfassung mehrerer Zutaten und Wiederholung einer ungültigen Ja/Nein-Eingabe
- Erstellung eines vollständigen Rezept-Dictionaries
- Vergabe der nächsten ID bei vorhandenen Rezepten und bei leerer Liste
- JSON-Speicherung und erneutes Laden nach einem Programmneustart
- Laden bei fehlender `recipes.json` → `[]`
- Laden bei ungültiger JSON-Datei → `json.JSONDecodeError` und Abbruch
- Import von `create_recipe()` ohne automatische Rezepterfassung; Start erst beim Funktionsaufruf

Diese Tests wurden manuell durchgeführt. Automatisierte Tests und die Integrationstests mit dem gemeinsamen Hauptmenü stehen noch aus.

## 9. Weitere Entwicklungsschritte

1. **US02:** Importformat und Importverhalten definieren; Importfunktion entwickeln und testen.
2. **Hauptmenü:** `create_recipe()` und die weiteren Gruppenfunktionen einbinden.
3. **Weitere User Storys:** Anzeige, Bearbeitung, Löschung, Skalierung, Einkaufsliste, Filter, Favoriten und Allergien nach Gruppenaufteilung integrieren.
4. **Qualitätssicherung:** Weitere Dateifehler und ungültige Datenstrukturen behandeln; gruppenübergreifende Tests durchführen.
5. **Dokumentation:** Funktionsbaum, Verantwortlichkeiten und Kontrollfluss bei weiteren Implementierungen aktualisieren.
