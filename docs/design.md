# Digitales Rezeptbuch – Programmdesign

## 1. Projektübersicht

Das Projekt ist eine lokale Python-Kommandozeilenanwendung (CLI), mit der ein Benutzer Rezepte erfassen, speichern, anzeigen, bearbeiten und verwalten kann.

## 2. Datenmodell

Alle Rezepte werden während der Programmausführung in einer Liste (`list`) verwaltet.

Jedes Rezept ist ein Dictionary (`dict`).

### 2.1 Rezept

| Feld | Datentyp | Beschreibung |
|---|---|---|
| id | int | Eindeutige Identifikationsnummer |
| name | str | Name des Rezepts |
| portions | int | Anzahl Portionen, grösser als 0 |
| ingredients | list | Liste von Zutaten |
| favorite | bool | Kennzeichnung als Favorit |
| allergies | list | Liste zugeordneter Allergietypen |

Neue Rezepte erhalten standardmässig `favorite = False` und eine leere Allergienliste.

### 2.2 Zutat

Jede Zutat wird ebenfalls als Dictionary dargestellt.

| Feld | Datentyp | Beschreibung |
|---|---|---|
| name | str | Name der Zutat |
| amount | float | Menge, grösser als 0 |
| unit | str | Einheit der Zutat |

Zulässige Einheiten: `g`, `ml`, `Stück`.

### 2.3 Identifikation

Jedes Rezept erhält eine eindeutige ID. Die ID wird nicht verändert, wenn das Rezept bearbeitet wird. Die ID muss innerhalb der aktuell gespeicherten Rezepte eindeutig sein. Beim Erstellen eines neuen Rezepts wird die höchste vorhandene ID um 1 erhöht. Falls noch keine Rezepte vorhanden sind, beginnt die Nummerierung bei 1. Gelöschte IDs dürfen später erneut vergeben werden.

## 3. Datenspeicherung

Die Speicherung erfolgt lokal in einer JSON-Datei.

Geplanter Speicherort: `data/recipes.json`

## 4. Grundprinzipien

- Eingabe, Verarbeitung und Ausgabe werden möglichst getrennt.
- Eine Funktion soll eine klar definierte Aufgabe erfüllen.
- Die Module verwenden das gemeinsame Datenmodell.
- Ungültige Benutzereingaben dürfen keinen Programmabbruch verursachen.
- Änderungen an Rezepten werden dauerhaft gespeichert.

## 5. Noch offene Entscheidungen

- Welche Allergietypen stehen zur Auswahl?
- Sind Rezepte ohne Zutaten zulässig?
- Wie werden eindeutige Rezept-IDs erzeugt?
- Welches konkrete Importformat verwendet US02?
- Wie soll das Programm bei einer fehlenden oder beschädigten JSON-Datei reagieren?
- Benötigen wir noch ein Feld für Freitext, in dem der User die Kochanweisungen aufschreiben kann?

## 6. Modulstruktur

Das Programm wird in mehrere Python-Module aufgeteilt. Jedes Modul übernimmt einen klar definierten Aufgabenbereich.

### 6.1 Modulübersicht und Verantwortlichkeiten

| Modul | Aufgabe | User Story | Verantwortlich |
|---|---|---|---|
| main.py | Programmstart, Hauptmenü und Ablaufsteuerung | US10 | Agshayan |
| recipe_input.py | Neue Rezepte erfassen | US01 | Alessandro |
| validation.py | Benutzereingaben überprüfen | US09 | Alessandro |
| storage.py | Rezeptdaten laden, speichern und importieren | US02 / gemeinsame Datenspeicherung | Alessandro / Team |
| recipe_management.py | Rezepte anzeigen, bearbeiten und löschen | US03, US04, US05 | Jennifer |
| recipe_tools.py | Zutatenmengen skalieren und Einkaufslisten erstellen | US06, US07 | Agshayan |
| recipe_features.py | Rezepte filtern, Favoriten und Allergien verwalten | US08, US11, US12 | Mai |

### 6.2 Zusammenarbeit der Module

- `main.py` steuert die Ausführung der verschiedenen Programmfunktionen.
- Die Rezepte werden beim Programmstart aus einer JSON-Datei geladen.
- Die anderen Module erhalten die benötigten Rezeptdaten zur Verarbeitung.
- Änderungen an Rezeptdaten werden über die Speicherfunktionen dauerhaft gespeichert.
- Die Funktionen zur Eingabevalidierung sollen von mehreren Modulen verwendet werden können.

### 6.3 Entwicklungsprinzipien

- Jedes Modul enthält logisch zusammengehörige Funktionen.
- Jede Funktion soll möglichst nur eine Aufgabe erfüllen.
- Eingabe, Verarbeitung und Ausgabe sollen soweit sinnvoll voneinander getrennt werden.
- Die gesamte Gruppe verwendet dasselbe Datenmodell.
- Jedes Gruppenmitglied entwickelt seine zugeteilten User Stories selbstständig.
- Änderungen am gemeinsamen Programm werden über GitHub dokumentiert.
- Die Modulverantwortlichkeiten und Schnittstellen werden innerhalb der Gruppe abgestimmt.

## 7. Function Tree

Die Anwendung wird in kleine, wiederverwendbare Funktionen unterteilt.

### 7.1 Hauptfunktionen

| Modul | Geplante Funktionen |
|---|---|
| main.py | main(), show_menu(), process_choice() |
| recipe_input.py | create_recipe(), input_ingredient() |
| validation.py | validate_text(), validate_portions(), validate_amount(), validate_unit() |
| storage.py | load_recipes(), save_recipes(), import_recipe() |
| recipe_management.py | show_recipes(), edit_recipe(), delete_recipe() |
| recipe_tools.py | scale_recipe(), create_shopping_list() |
| recipe_features.py | filter_recipes(), manage_favorites(), manage_allergies() |

Die Funktionsnamen sind vorläufig und werden bei der Implementierung geprüft.

### 7.2 Grundsätze

- Jede Funktion soll möglichst genau eine Aufgabe erfüllen.
- Gemeinsam benötigte Funktionen werden wiederverwendet.
- Die Module tauschen Daten über klar definierte Parameter und Rückgabewerte aus.
- Die Datei `main.py` koordiniert den Programmablauf.

## 8. Main Decision and Control Flow

### 8.1 Programmstart

1. Das Programm wird gestartet.
2. Bereits gespeicherte Rezepte werden aus der JSON-Datei geladen.
3. Das Hauptmenü wird angezeigt.

### 8.2 Menüsteuerung

1. Der Benutzer gibt eine Menüauswahl ein.
2. Die Eingabe wird geprüft.
3. Bei ungültiger Auswahl erscheint eine Fehlermeldung.
4. Bei gültiger Auswahl wird die entsprechende Funktion ausgeführt.
5. Nach Abschluss einer Funktion wird das Hauptmenü erneut angezeigt.
6. Dieser Ablauf wiederholt sich, bis der Benutzer das Programm beendet.

### 8.3 Datenänderungen

- Beim Erfassen, Bearbeiten oder Löschen von Rezepten werden die Rezeptdaten geändert.
- Änderungen an Favoriten und Allergien werden ebenfalls gespeichert.
- Die Daten werden nach erfolgreichen Änderungen in die JSON-Datei geschrieben.
- Die Skalierung von Zutaten verändert das ursprüngliche Rezept nicht.

### 8.4 Kontrollstrukturen

- `if`, `elif`, `else`: Menüentscheidungen und Eingabeprüfung
- `while`: Wiederholung des Hauptmenüs und gegebenenfalls von Benutzereingaben
- `for`: Verarbeitung mehrerer Rezepte oder Zutaten

### 8.5 Fehlerbehandlung

Ungültige Benutzereingaben sollen verständliche Fehlermeldungen auslösen, ohne das Programm zu beenden.

Fehler beim Lesen und Schreiben von Dateien müssen ebenfalls behandelt werden. Das genaue Verhalten wird während der Implementierung festgelegt.

### 8.6 Control Flow – US01 Rezeptnamenvalidierung

**Ziel:** Sicherstellen, dass der Benutzer einen gültigen, nicht leeren Rezeptnamen eingibt.

**Zuständige Module:**
- `recipe_input.py`: Benutzereingabe und Wiederholung
- `validation.py`: Überprüfung des Rezeptnamens

**Geplanter Ablauf:**

1. Das Programm fordert den Benutzer auf, einen Rezeptnamen einzugeben.
2. Die Eingabe wird als String (`str`) entgegengenommen.
3. Der eingegebene Text wird an `validate_text()` übergeben.
4. Die Funktion prüft, ob der Text nach dem Entfernen führender und nachgestellter Leerzeichen leer ist.
5. Ist der Text leer, gibt `validate_text()` den Boolean `False` zurück.
6. `recipe_input.py` erkennt den ungültigen Rückgabewert und zeigt eine verständliche Fehlermeldung an.
7. Die Eingabe wird mithilfe einer `while`-Schleife wiederholt.
8. Ist der Text gültig, gibt `validate_text()` den Boolean `True` zurück.
9. Die Eingabeschleife wird beendet und der gültige Rezeptname übernommen.
10. Das Programm fährt mit der Eingabe der Portionszahl fort.

**Verwendete Python-Konzepte:**
- `input()` zur Erfassung des Rezeptnamens
- `str` als Datentyp
- `strip()` zum Entfernen führender und nachgestellter Leerzeichen
- `if` / `else` zur Gültigkeitsprüfung
- `while` zur Wiederholung ungültiger Eingaben
- `return` zur Rückgabe von `True` oder `False`

**Rückgabewerte von `validate_text()`:**

| Eingabe | Rückgabewert |
|---|---|
| `"Spaghetti Napoli"` | `True` |
| `"   "` | `False` |
| `""` | `False` |
| `"Risotto"` | `True` |

**Architekturentscheidung:**

Die Validierungsfunktion überprüft ausschliesslich den übergebenen Text. Sie fordert selbst keine Benutzereingaben an und gibt keine Fehlermeldungen aus.

Dadurch kann die Funktion auch in anderen Modulen, beispielsweise beim Bearbeiten eines Rezeptnamens, wiederverwendet werden.

### 8.7 Control Flow – US01 Portionsvalidierung

**Ziel:** Der Benutzer muss eine gültige positive Ganzzahl für die Anzahl Portionen eingeben.

**Zuständige Module:**
- `recipe_input.py`: Benutzereingabe und Wiederholung
- `validation.py`: Umwandlung und Validierung

**Geplanter Ablauf:**

1. Das Programm fordert den Benutzer auf, die Anzahl Portionen einzugeben.
2. Die Eingabe wird als String entgegengenommen.
3. `validate_portions()` versucht, den String in einen Integer umzuwandeln.
4. Ist die Umwandlung nicht möglich, wird der `ValueError` abgefangen und `None` zurückgegeben.
5. Bei erfolgreicher Umwandlung wird geprüft, ob die Zahl grösser als 0 ist.
6. Wenn die Zahl kleiner oder gleich 0 ist, wird `None` zurückgegeben.
7. Wenn die Zahl positiv ist, wird der Integer zurückgegeben.
8. Erhält `recipe_input.py` den Wert `None`, wird eine Fehlermeldung angezeigt und erneut nach der Portionszahl gefragt.
9. Sobald eine gültige Portionszahl vorliegt, wird die Eingabeschleife beendet.
10. Das Programm fährt mit der Erfassung der Zutaten fort.

**Verwendete Python-Konzepte:**
- `input()` zur Eingabe von Daten
- `int()` zur Datentypumwandlung
- `try` / `except ValueError` zur Fehlerbehandlung
- `if` zur Prüfung des Zahlenbereichs
- `while` zur Wiederholung ungültiger Eingaben
- `return` zur Rückgabe eines Integers oder `None`

### 8.8 Control Flow – US01 Zutatenerfassung

**Ziel:** Der Benutzer kann eine oder mehrere Zutaten erfassen. Jede Zutat enthält einen Namen, eine Menge und eine Einheit.

**Architekturentscheidungen:**
- Ein Rezept muss mindestens eine Zutat enthalten.
- Jede Zutat wird als Dictionary (`dict`) dargestellt.
- Alle Zutaten eines Rezepts werden in einer Liste (`list`) gesammelt.
- Zulässige Einheiten sind `g`, `ml` und `Stück`.
- Ungültige Eingaben werden erneut angefordert, ohne bereits gültige Eingaben zu verlieren.

**Zuständige Module:**
- `recipe_input.py`: Erfassung einzelner Zutaten, Schleifensteuerung und Erstellung der Zutatenliste
- `validation.py`: Überprüfung der Eingaben

#### 8.8.1 Einzelne Zutat erfassen

Geplante Funktion: `input_ingredient()`

1. Das Programm fordert den Benutzer auf, einen Zutatennamen einzugeben.
2. Der Zutatenname wird mit `validate_text()` überprüft.
3. Ist der Name ungültig, erscheint eine Fehlermeldung und die Namenseingabe wird wiederholt.
4. Das Programm fordert den Benutzer auf, eine Menge einzugeben.
5. `validate_amount()` versucht, die Eingabe in einen `float` umzuwandeln.
6. Die Menge muss grösser als 0 sein. Bei einer ungültigen Eingabe wird `None` zurückgegeben.
7. Bei `None` wird eine Fehlermeldung angezeigt und ausschliesslich die Mengenabfrage wiederholt.
8. Anschliessend wird die Einheit erfasst.
9. `validate_unit()` prüft, ob die Einheit `g`, `ml` oder `Stück` ist.
10. Bei einer ungültigen Einheit wird nur die Einheitenabfrage wiederholt.
11. Sobald alle drei Werte gültig sind, wird ein Zutaten-Dictionary erstellt.
12. Die Funktion gibt das vollständige Zutaten-Dictionary zurück.

#### 8.8.2 Mehrere Zutaten erfassen

1. Eine leere Zutatenliste (`ingredients`) wird erstellt.
2. `input_ingredient()` wird aufgerufen.
3. Das zurückgegebene Zutaten-Dictionary wird mit `append()` zur Liste hinzugefügt.
4. Das Programm fragt: „Weitere Zutat erfassen? (j/n)“.
5. Die Eingabe wird durch `validate_yes_no()` überprüft.
6. Bei `True` beginnt ein weiterer Durchlauf zur Erfassung einer neuen Zutat.
7. Bei `False` wird die Zutatenschleife beendet.
8. Bei `None` erscheint eine Fehlermeldung und ausschliesslich die Ja/Nein-Abfrage wird wiederholt.
9. Die vollständige Zutatenliste wird für die Erstellung des Rezept-Dictionarys bereitgestellt.

#### 8.8.3 Rückgabewerte

| Funktion | Gültige Rückgabe | Ungültige Rückgabe |
|---|---|---|
| validate_text() | True | False |
| validate_amount() | Positiver float | None |
| validate_unit() | True | False |
| validate_yes_no() | True oder False | None |
| input_ingredient() | Zutaten-Dictionary | Keine Rückgabe bei ungültiger Eingabe, da diese wiederholt wird |

#### 8.8.4 Verwendete Python-Konzepte

- `input()` zur Erfassung von Benutzereingaben
- `str` für Zutatenname und Einheit
- `float` für die Zutatenmenge
- `dict` zur Speicherung einer einzelnen Zutat
- `list` zur Speicherung mehrerer Zutaten
- `append()` zum Hinzufügen von Zutaten
- `while` zur Wiederholung von Eingaben und zur Erfassung mehrerer Zutaten
- `if` / `else` zur Entscheidungssteuerung
- `try` / `except ValueError` zur Behandlung ungültiger Mengeneingaben
- `return` zur Übergabe validierter Werte und vollständiger Zutaten

### 8.9 Control Flow – US01 Rezept erstellen und speichern

**Ziel:** Die gültig erfassten Rezeptdaten werden zu einem vollständigen Rezept zusammengefügt und dauerhaft gespeichert.

**Zuständige Module:**
- `recipe_input.py`: Rezept erstellen und zur Rezeptliste hinzufügen
- `storage.py`: Rezeptliste dauerhaft speichern

#### 8.9.1 Rezept-Dictionary erstellen

1. Der gültige Rezeptname liegt als String vor.
2. Die gültige Portionszahl liegt als Integer vor.
3. Die erfassten Zutaten liegen als Liste von Dictionaries vor.
4. Die höchste vorhandene Rezept-ID wird ermittelt.
5. Die neue Rezept-ID wird durch Erhöhung der höchsten ID um 1 bestimmt. Bei einer leeren Rezeptliste wird die ID 1 vergeben.
6. Ein neues Rezept-Dictionary wird erstellt.

Das Rezept-Dictionary enthält folgende Felder:

| Feld | Wert |
|---|---|
| id | Neue eindeutige Rezept-ID |
| name | Validierter Rezeptname |
| portions | Validierte Portionszahl |
| ingredients | Liste der erfassten Zutaten |
| favorite | False |
| allergies | Leere Liste |

7. Das vollständige Rezept-Dictionary wird mit `append()` zur Liste `recipes` hinzugefügt.

#### 8.9.2 Rezept dauerhaft speichern

1. Die aktualisierte Rezeptliste wird an `save_recipes()` übergeben.
2. `save_recipes()` befindet sich im Modul `storage.py`.
3. Die Rezeptliste wird in der Datei `data/recipes.json` gespeichert.
4. Nach erfolgreicher Speicherung erscheint eine Bestätigung.
5. Anschliessend kehrt das Programm zum Hauptmenü zurück.

#### 8.9.3 Fehlerbehandlung

- Schlägt die Speicherung fehl, erscheint eine verständliche Fehlermeldung.
- Das Programm darf eine fehlgeschlagene Speicherung nicht als erfolgreich bestätigen.
- Das weitere Vorgehen nach einem Speicherfehler wird bei der Implementierung von `storage.py` festgelegt.

#### 8.9.4 ID-Vergabe

Jedes Rezept besitzt eine numerische ID.

Die ID muss innerhalb der aktuell gespeicherten Rezepte eindeutig sein.

Neue IDs werden anhand der höchsten vorhandenen ID vergeben:

- Höchste ID + 1
- Falls keine Rezepte existieren: ID 1

Gelöschte IDs dürfen später erneut verwendet werden.

#### 8.9.5 Verwendete Python-Konzepte

- `dict` zur Erstellung des Rezepts
- `list` zur Verwaltung mehrerer Rezepte
- `append()` zum Hinzufügen des Rezepts
- `max()` als mögliche Hilfsfunktion zur ID-Ermittlung
- `if` / `else` für Entscheidungen
- `return` zur Übergabe von Ergebnissen
- JSON-Dateiverarbeitung für die permanente Speicherung

#### 8.9.6 Architekturprinzip

Die Erstellung eines Rezepts und das dauerhafte Speichern werden logisch getrennt.

Die Zuständigkeit für die Dateiverarbeitung liegt bei `storage.py`, damit dieselben Speicherfunktionen auch von anderen Modulen verwendet werden können.