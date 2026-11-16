# Digitales Rezeptbuch – Programmdesign

## 1. Projektübersicht

Das Projekt ist eine lokale Python-Kommandozeilenanwendung (CLI), mit der Benutzer Rezepte erfassen, speichern, anzeigen, bearbeiten und verwalten können. Die Anwendung wird von vier Gruppenmitgliedern gemeinsam entwickelt. Die einzelnen Funktionen werden auf mehrere Python-Module verteilt.

**Dokumentationsstand (November 2026):** Die Rezepterfassung (US01), der Rezeptimport (US02) und die Eingabe-/Importvalidierung (US09) sind implementiert und manuell getestet. Die Rückmeldungen des Dozenten wurden in den Eingabeaufforderungen, der Ausgabe nach der Rezepterfassung und der Allergieauswahl berücksichtigt. Das Hauptmenü ist vorhanden und startet bereits Rezepterfassung, Rezeptimport, eine einfache Rezeptliste, Skalierung und Einkaufsliste; weitere Menüpunkte sind noch Platzhalter. Weitere Funktionen sind in separaten Modulen vorhanden, aber nicht alle mit dem Hauptmenü verbunden. Als Quelle für den dokumentierten Implementierungsstand dient der hochgeladene Projektstand; nicht integrierte Teile werden ausdrücklich als solche bezeichnet.

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

Bei der **manuellen Rezepterfassung** wird `favorite = False` gesetzt; `allergies` enthält die vom Benutzer über eine nummerierte Liste ausgewählten Allergien oder `[]`, wenn die Auswahl mit `fertig` ohne Eintrag beendet wird. Beim **JSON-Import** werden `favorite = False` und `allergies = []` gesetzt, da die Importdatei nur Name, Portionen und Zutaten liefern muss. Die Favoritenverwaltung und Allergiefilterung befinden sich in `recipe_features.py`.

Beispiel eines manuell erfassten Rezepts mit ausgewählten Allergien:

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
    "allergies": ["Gluten", "Laktose"]
}
```

### 2.2 Zutat

Jede Zutat wird ebenfalls als Dictionary dargestellt.

| Feld | Datentyp | Beschreibung |
|---|---|---|
| `name` | `str` | Name der Zutat; darf nicht leer sein |
| `amount` | `float` (manuelle Eingabe); `int` oder `float` (JSON-Import) | Endliche, positive Menge, grösser als 0 |
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

- Eingabe, Verarbeitung und Ausgabe werden möglichst getrennt; `recipe_input.py` vereint derzeit Eingabe, Ablaufkoordination und die Ausgabe des neu erfassten Rezepts.
- Eine Funktion soll eine klar definierte Aufgabe erfüllen; vorhandene Funktionen werden wiederverwendet.
- Die Module verwenden das gemeinsame Datenmodell.
- Eingaben der manuellen Rezepterfassung werden als **Aufforderungen statt Fragen** formuliert, zum Beispiel `Rezeptname eingeben: `. Hinter dem Doppelpunkt steht ein Leerzeichen vor der Eingabe.
- Ungültige Benutzereingaben sollen keinen Programmabbruch verursachen, sondern erneut abgefragt werden.
- Rezeptänderungen werden dauerhaft gespeichert.
- Beschädigte gespeicherte Daten dürfen nicht stillschweigend überschrieben werden.
- Die Allergiezuordnung gehört zur manuellen Rezepterfassung (US01), nicht mehr zu einer separat zu entwickelnden User Story. Bestehende Allergiefilter-Funktionen bleiben erhalten.
- Änderungen werden auf separaten Git-Branches entwickelt und erst nach Kontrolle per Pull Request in `main` übernommen.

## 5. Getroffene und offene Entscheidungen

### 5.1 Getroffene Entscheidungen

- Ein Rezept muss mindestens eine Zutat enthalten.
- Die aktuell erlaubten Einheiten sind `g`, `ml` und `Stück`.
- Rezept-IDs werden nach der Regel *höchste vorhandene ID + 1* vergeben; bei leerer Liste beginnt die Zählung bei 1.
- Bei manueller Erfassung wird `favorite = False` gesetzt und die Allergien werden direkt abgefragt; der Benutzer darf auch keine Allergien auswählen.
- Beim Import werden `favorite = False` und `allergies = []` vergeben. Im gespeicherten Rezept werden nur die vorgesehenen Felder auf **Rezept-Ebene** übernommen; die Zutaten-Dictionaries bleiben bei der Übernahme unverändert.
- Eine fehlende `data/recipes.json` führt beim Laden zu einer leeren Rezeptliste.
- Eine gespeicherte JSON-Datei mit ungültigem Inhalt verursacht eine Fehlermeldung und einen Abbruch des aktuellen Ablaufs, damit sie nicht überschrieben wird.
- Die dauerhafte Datenspeicherung erfolgt über `storage.py`.
- Die Allergietypen lauten `Gluten`, `Laktose`, `Nüsse`, `Eier`, `Soja`, `Sesam`, `Krebstiere`, `Weichtiere` und sind in `recipe_features.py` definiert.
- Die manuelle Allergieauswahl erfolgt über Nummern von 1 bis 8 und endet mit `fertig`.
- Der Zutatenfilter (US08) zeigt nur Rezepte, die **alle** eingegebenen Zutaten enthalten. Der Vergleich ignoriert Gross-/Kleinschreibung, verlangt aber den exakten Zutatennamen (`mehl` findet `Mehl`, aber nicht `Dinkelmehl`).
- Der Allergiefilter zeigt nur Rezepte, die **keine** der eingegebenen Allergien enthalten. Die Allergien werden beim Filtern als Text eingegeben (nicht als Nummer), Gross-/Kleinschreibung spielt keine Rolle.
- In der Favoritenverwaltung (US11) fragt `edit_favorites()` zuerst, ob Favoriten angezeigt oder bearbeitet werden sollen.

### 5.2 Noch offene Entscheidungen

- Benötigt das Rezept zusätzlich ein Feld für Freitext/Kochanweisungen? (Noch nicht entschieden.)
- Wie sollen Schreibfehler bei der Dateispeicherung und fehlerhafte Datenstrukturen in der **gespeicherten** Rezeptdatei (bei syntaktisch gültigem JSON) behandelt werden?
- Sollen die Einheiten- und Ja/Nein-Eingaben später auch alternative Schreibweisen erlauben (z. B. `stück`, `J`)?
- Wie werden die bereits vorhandenen, aber noch nicht verdrahteten Anzeige-, Lösch- und Filterfunktionen ins Hauptmenü integriert?

## 6. Modulstruktur

Das Programm ist in mehrere Python-Module aufgeteilt. Jedes Modul übernimmt einen möglichst klar abgegrenzten Aufgabenbereich.

### 6.1 Modulübersicht und Verantwortlichkeiten

| Modul | Aktuelle Aufgabe | User Story / Bezug | Zuständigkeit im Team |
|---|---|---|---|
| `main.py` | Programmstart und Hauptmenü (`show_menu()`, `main()`); Aufruf weiterer Funktionen; mehrere Menüoptionen noch Platzhalter | US10 / Integration | Agshayan / Team |
| `recipe_input.py` | Eingabe von Rezeptnamen, Portionen und Zutaten; `ask_recipe()`, `create_recipe()` und `import_new_recipe()`; leserliche Ausgabe nach manueller Erfassung | US01, US02, Dozentenfeedback | Alessandro |
| `validation.py` | Eingabe- und Rezeptimportvalidierung (`validate_import_recipe()`) | US09, US02 | Alessandro |
| `storage.py` | Laden/Speichern der Rezeptliste und Einlesen/Prüfen einer Importdatei (`import_recipe()`) | Datenspeicherung, US02 | Alessandro / Team |
| `recipe_management.py` | Eindeutige Rezept-IDs ermitteln und zuweisen | US01, US02 | Alessandro |
| `recipe_tools.py` | Zutatenmengen skalieren und Einkaufslisten erzeugen | US06, US07 | Agshayan |
| `recipe_features.py` | Allergieauswahl bei der Eingabe, Zutaten-/Allergiefilter und Favoritenverwaltung | US01 (Allergien), US08, US11 | Allergieauswahl: Mai, eingebunden von Alessandro; übrige Features: Mai |
| `recipe_display.py` | `show_recipes()` zur Anzeige und Auswahl gespeicherter Rezepte; aktuell nicht über Menüpunkt 3 aufgerufen | US03 | Jennifer |
| `recipe_delete.py` | `delete_recipe()` mit Bestätigung und Speicherung; aktuell nicht über Menüpunkt 5 aufgerufen | US05 | Jennifer |

### 6.2 Zusammenarbeit der Module

- `main.py` zeigt das Hauptmenü und ruft bei den Menüoptionen 1 und 2 die Funktionen `create_recipe()` bzw. `import_new_recipe()` aus `recipe_input.py` auf.
- `recipe_input.py` verwendet die Prüfungen aus `validation.py` und ruft für die Allergieauswahl `ask_recipe_allergies()` aus `recipe_features.py` auf.
- `create_recipe()` und `import_new_recipe()` liegen **nicht mehr in `main.py`**, sondern in `recipe_input.py`. Dort laden sie bestehende Daten, vergeben IDs über `recipe_management.py` und speichern über `storage.py`.
- `recipe_features.py` verwendet `storage.py`, um bei Filtern und Favoriten die gespeicherten Rezepte zu laden bzw. zu aktualisieren.
- `recipe_tools.py` stellt Skalierung und Einkaufsliste für die Menüpunkte 6 und 7 bereit.
- Die Module `recipe_display.py` und `recipe_delete.py` enthalten eigene Funktionen. Im aktuellen Hauptmenü werden diese noch nicht aufgerufen.
- Die Menüoptionen 4, 5, 8, 9 und 10 enthalten derzeit `pass` und führen noch keine Fachfunktion aus; Option 3 gibt lediglich eine nummerierte Namensliste aus.

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

### 7.1 Im hochgeladenen Projektstand implementierte Funktionen

| Modul | Funktion | Aufgabe |
|---|---|---|
| `main.py` | `show_menu()`, `main()` | Menü anzeigen, Benutzereingabe entgegennehmen und vorhandene Menüpunkte steuern |
| `recipe_input.py` | `create_recipe()` | Manuell erfasstes Rezept mit neuer ID speichern und leserlich ausgeben |
| `recipe_input.py` | `import_new_recipe(file_path)` | Gültige Importdaten übernehmen, ID/Standardfelder ergänzen und speichern |
| `recipe_input.py` | `ask_recipe()` | Rezeptdaten ohne ID inklusive Allergieauswahl erfassen |
| `recipe_input.py` | `ask_recipe_name()`, `ask_portions()` | Rezeptname und Portionszahl mit Validierung erfassen |
| `recipe_input.py` | `ask_ingredients()`, `ask_ingredient()` | Zutatenliste und einzelne Zutat erfassen |
| `recipe_input.py` | `ask_ingredient_name()`, `ask_ingredient_amount()`, `ask_ingredient_unit()` | Zutatenfelder mit Validierung erfassen |
| `recipe_features.py` | `ask_recipe_allergies()` | Allergien nummeriert auswählen; Mehrfachnennung verhindern; Abschluss mit `fertig` |
| `validation.py` | `validate_text()`, `validate_portions()`, `validate_amount()` | Text sowie positive Portionen/Mengen überprüfen |
| `validation.py` | `validate_unit()`, `validate_yes_no()` | Erlaubte Einheiten und `j`/`n` prüfen |
| `validation.py` | `validate_import_recipe(recipe)` | Struktur und Pflichtwerte eines JSON-Rezepts überprüfen |
| `recipe_management.py` | `generate_next_id(recipes)`, `add_recipe_id(recipe, recipes)` | Eindeutige ID berechnen und vergeben |
| `storage.py` | `load_recipes()`, `save_recipes(recipes)`, `import_recipe(file_path)` | Gespeicherte Rezepte laden/sichern, Importdatei einlesen und validieren |
| `recipe_tools.py` | `scale_recipe()`, `create_shopping_list()` | Mengen skalieren und Einkaufsliste erstellen |
| `recipe_features.py` | `input_ingredients()`, `ingredient_filter()` | Suchzutaten erfassen und passende Rezepte ermitteln |
| `recipe_features.py` | `user_input_allergies()`, `allergies_filter()` | Allergien für die Filterung erfassen und Rezepte mit diesen Allergien ausschliessen |
| `recipe_features.py` | `user_input1_favorites()`, `user_input2_favorites()` | ID und Favoritenaktion abfragen |
| `recipe_features.py` | `get_favorites()`, `edit_favorites()` | Favoriten anzeigen, setzen und entfernen |
| `recipe_display.py` | `show_recipes()` | Rezepte auflisten und Details eines ausgewählten Rezepts zeigen; noch nicht im Menü verdrahtet |
| `recipe_delete.py` | `delete_recipe()` | Rezept mit Bestätigung löschen; noch nicht im Menü verdrahtet |

### 7.2 Noch nicht integrierte oder offene Funktionen

- `main.py`: Menüoptionen 4 (Bearbeiten), 5 (Löschen), 8 (Zutatenfilter), 9 (Favoriten) und 10 (Allergien) sind noch `pass`-Platzhalter.
- `main.py`: Bei Option 3 wird eine einfache nummerierte Namensliste ausgegeben. Die bereits vorhandene Detailfunktion `show_recipes()` aus `recipe_display.py` ist noch nicht verbunden.
- `recipe_management.py`: Die Bearbeitung von Rezepten ist im hochgeladenen Stand dort noch nicht implementiert.
- `recipe_features.py`: Eine eigenständige nachträgliche Allergiebearbeitung (`edit_allergies()`) ist im hochgeladenen Code **nicht vorhanden**. Die Allergieauswahl ist stattdessen direkt in US01 integriert; die Allergiefilterung ist separat vorhanden.

Funktionsnamen und Aufgaben weiterer Umsetzungen werden erst nach tatsächlicher Implementierung verbindlich dokumentiert.

### 7.3 Grundsätze

- Funktionen werden möglichst für genau eine Aufgabe eingesetzt.
- Gemeinsam benötigte Funktionen werden wiederverwendet.
- Die Module tauschen Daten über Parameter und Rückgabewerte aus.
- `main.py` koordiniert den Ablauf, während andere Module Eingabe, Validierung, Verwaltung und Speicherung übernehmen.

## 8. Main Decision and Control Flow

### 8.1 Programmstart

1. Beim direkten Start von `main.py` wird durch `if __name__ == "__main__":` die Funktion `main()` aufgerufen.
2. `main()` zeigt mit `show_menu()` das Hauptmenü an.
3. Die gespeicherten Rezepte werden nicht pauschal beim Programmstart, sondern bei Bedarf durch die jeweilige Menüfunktion mit `load_recipes()` geladen.
4. Die Menüsteuerung läuft in einer `while True`-Schleife, bis der Benutzer `0` auswählt.

**Aktuell implementiert:** Hauptmenü mit funktionsfähigen Aufrufen für Rezepterfassung (1), Import (2), einfache Rezeptliste (3), Skalierung (6) und Einkaufsliste (7). Nicht alle übrigen Optionen sind integriert.

### 8.2 Menüsteuerung (teilweise implementiert)

1. `show_menu()` zeigt die Optionen `0` bis `10` an.
2. `main()` liest die Auswahl mit `input("Wähle eine Option: ")` ein.
3. `0` beendet die Schleife.
4. `1` ruft `create_recipe()` aus `recipe_input.py` auf; `2` fordert einen Dateipfad an und ruft `import_new_recipe(file_path)` auf.
5. `3` lädt die Rezeptliste und gibt Nummer und Rezeptname aus (noch ohne Aufruf von `recipe_display.show_recipes()`).
6. `6` und `7` laden die Rezepte, lassen eine Rezeptnummer auswählen und rufen `scale_recipe()` bzw. `create_shopping_list()` auf.
7. `4`, `5`, `8`, `9`, `10` sind derzeit mit `pass` vorgesehen. Nicht aufgeführte Auswahlen erhalten die Meldung „Diese Option ist nicht verfügbar.“
8. Danach wird das Menü erneut angezeigt.

### 8.3 Datenänderungen

- Beim Erfassen, Bearbeiten oder Löschen von Rezepten werden Rezeptdaten geändert.
- Änderungen an Favoriten werden in `recipe_features.py` gespeichert; Allergien werden bei der manuellen Rezepterfassung ausgewählt und zusammen mit dem Rezept gespeichert.
- Die Daten werden nach erfolgreichen Änderungen in die JSON-Datei geschrieben.
- Die implementierte Skalierung erstellt ein neues Rezept-Dictionary und eine neue Zutatenliste, ohne die gespeicherten Rezeptmengen zu verändern.

### 8.4 Kontrollstrukturen

- `if`, `elif`, `else`: Entscheidungen und Eingabeprüfung
- `while`: Wiederholung ungültiger Eingaben, mehrerer Zutaten, der Allergieauswahl und des Hauptmenüs
- `for`: Durchlaufen von Zutaten, Allergien und Rezepten (Ausgabe, Filterung und ID-Vergabe)
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

1. `ask_portions()` fordert die Portionszahl mit `Anzahl Portionen eingeben: ` an.
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
4. Jede ungültige Teilangabe führt zu einer Fehlermeldung und einer erneuten Aufforderung für genau diese Angabe.
5. `ask_ingredient()` erstellt und gibt ein Dictionary mit den Schlüsseln `name`, `amount` und `unit` zurück.

#### 8.8.2 Mehrere Zutaten erfassen

**Implementierte Funktion:** `ask_ingredients()`

1. Eine leere Zutatenliste `ingredients` wird erstellt.
2. Eine äussere `while`-Schleife erfasst mindestens eine Zutat mit `ask_ingredient()`.
3. Das Zutaten-Dictionary wird mit `ingredients.append(ingredient)` ergänzt.
4. Der Benutzer wird mit `Weitere Zutat hinzufügen (j/n): ` aufgefordert, sich für eine weitere Zutat zu entscheiden.
5. `validate_yes_no()` gibt bei `j` `True`, bei `n` `False`, sonst `None` zurück.
6. Eine innere `while`-Schleife wiederholt die Ja/Nein-Eingabeaufforderung, solange das Ergebnis `None` ist.
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

**Ziel:** Gültige Rezeptdaten samt Allergieauswahl zu einem vollständigen Rezept zusammenführen, eine ID vergeben, dauerhaft speichern und nach der Erfassung übersichtlich ausgeben.

**Zuständige Module:**

- `recipe_input.py`: `ask_recipe()` (Erfassung), `create_recipe()` (Ablauf und Ausgabe)
- `recipe_features.py`: `ask_recipe_allergies()` (Allergieauswahl aus einer nummerierten Liste)
- `recipe_management.py`: `generate_next_id()` und `add_recipe_id()` (ID-Vergabe)
- `storage.py`: `load_recipes()` und `save_recipes()` (Dateiverarbeitung)
- `main.py`: Aufruf von `create_recipe()` über Menüoption 1

#### 8.9.1 Rezept-Dictionary erstellen

1. `ask_recipe()` ruft `ask_recipe_name()`, `ask_portions()` und `ask_ingredients()` auf.
2. Anschliessend ruft die Funktion `ask_recipe_allergies()` aus `recipe_features.py` auf.
3. Die Allergien werden mit Nummern 1 bis 8 gewählt. `fertig` beendet die Auswahl; eine leere Liste ist zulässig. Ungültige und doppelte Nummern werden zurückgewiesen.
4. `ask_recipe()` erstellt ein Dictionary mit `name`, `portions`, `ingredients`, `favorite = False` und den ausgewählten `allergies`; die ID fehlt noch.
5. `generate_next_id(recipes)` ermittelt die höchste bereits vorhandene ID und erhöht sie um 1. `add_recipe_id(recipe, recipes)` fügt die neue ID hinzu.

#### 8.9.2 Vollständigen Ablauf ausführen und speichern

Die Funktion `create_recipe()` in **`recipe_input.py`** führt diese Schritte aus:

1. `load_recipes()` lädt die bestehende Rezeptliste.
2. `ask_recipe()` erfasst Name, Portionen, Zutaten und Allergien.
3. `add_recipe_id(recipe, recipes)` ergänzt eine eindeutige ID.
4. `recipes.append(recipe)` fügt das Rezept zur Liste hinzu.
5. `save_recipes(recipes)` schreibt die aktualisierte Liste nach `data/recipes.json`.
6. Statt `print(recipes)` gibt die Funktion den neuen Rezeptnamen, die Portionszahl und jede Zutat als `- Menge Einheit Name` aus. Anschliessend folgt die Allergienliste mit einem eigenen Eintrag je ausgewählter Allergie.

Beispiel für die Konsolenausgabe nach erfolgreicher Erfassung:

```text
Rezept: Pfannkuchen
Portionen: 2
Zutaten:
- 250.0 g Mehl
- 200.0 ml Milch
Allergien:
- Gluten
- Laktose
```

Bei einer leeren Allergienliste wird aktuell trotzdem `Allergien:` ausgegeben, aber kein Aufzählungspunkt. Die Ausgabe ist Teil von `create_recipe()` und damit noch keine zentrale Formatierungsfunktion für alle Menüpunkte.

#### 8.9.3 Fehlerbehandlung und Datensicherheit

- `load_recipes()` behandelt `FileNotFoundError` mit einer leeren Rezeptliste `[]`.
- `load_recipes()` behandelt `json.JSONDecodeError` mit einer Fehlermeldung und `raise`; der Ablauf wird vor `save_recipes()` abgebrochen.
- Eingabefunktionen wiederholen ungültige Angaben, sodass zuvor erfasste gültige Werte nicht verloren gehen.
- `save_recipes()` schreibt derzeit im Modus `"w"` und verwendet keine spezielle Behandlung von Schreibfehlern.

#### 8.9.4 ID-Vergabe

Die ID entspricht der höchsten ID der aktuell vorhandenen Rezepte plus 1; bei einer leeren Liste beginnt sie bei 1. Die Implementierung verwendet `highest_id = 0`, eine `for`-Schleife und einen Vergleich, nicht `max()`.

#### 8.9.5 Verwendete Python-Konzepte

`dict`, `list`, `append()`, `for`, `while`, `if`, `return`, f-Strings, Funktionsparameter und Rückgabewerte, Modul-Imports, `with open()`, `json.dump()`, `json.load()`, `try`/`except`, `raise`.

#### 8.9.6 Architekturprinzip

`main.py` verwaltet das Hauptmenü. `recipe_input.py` enthält den Erfassungsablauf und die anschliessende Konsolenausgabe; `recipe_features.py` liefert die Allergieauswahl, `recipe_management.py` die ID und `storage.py` die Dateiverarbeitung. Die Funktionen arbeiten mit dem gemeinsamen Rezept-Dictionary.

### 8.10 Manuelle Tests – US01 und Dozentenfeedback

Folgende Verhaltensweisen wurden während der Entwicklung manuell geprüft:

- Gültige und ungültige Rezeptnamen sowie Portionszahlen.
- Gültige und ungültige Zutatenangaben einschliesslich negativer Mengen und `inf`.
- Erfassung mehrerer Zutaten und Wiederholung einer ungültigen Ja/Nein-Eingabe.
- Erstellung eines vollständigen Rezept-Dictionaries sowie Vergabe einer eindeutigen ID.
- JSON-Speicherung und erneutes Laden nach einem Programmneustart; Ladefehler bei fehlender oder beschädigter Datei.
- Alle sechs Eingabeaufforderungen in `recipe_input.py` wurden auf Befehlsform und Leerzeichen vor der Eingabe geprüft.
- `ask_recipe_allergies()` wurde mit den Nummern `1`, `3` und `fertig` getestet (`['Gluten', 'Nüsse']`).
- Die Übernahme der ausgewählten Allergien durch `ask_recipe()` und ihre Speicherung über `create_recipe()` wurden manuell geprüft.
- Die leserliche Konsolenausgabe von Name, Portionen, Zutaten und Allergien wurde nach der Erfassung geprüft.

**Abgrenzung:** Die dokumentierten Tests erfolgten manuell im Rahmen der Entwicklung. Ein vollständiger automatisierter Testlauf für sämtliche Module und Menüfunktionen ist nicht belegt.

## US02 – Rezept importieren

### Beschreibung

Benutzer können ein einzelnes Rezept aus einer lokalen JSON-Datei importieren. Es wird vor dem Speichern validiert und der bestehenden Rezeptliste hinzugefügt.

### Importformat

Die Importdatei enthält ein JSON-Objekt mit genau einem Rezept. Erforderliche Felder auf Rezept-Ebene:

| Feld | Datentyp | Regel |
|---|---|---|
| `name` | String | Nicht leer, nicht nur Leerzeichen |
| `portions` | Integer | Positive Ganzzahl; `bool` wird nicht akzeptiert |
| `ingredients` | Liste | Mindestens eine Zutat |

Jede Zutat muss folgende Felder enthalten:

| Feld | Datentyp | Regel |
|---|---|---|
| `name` | String | Nicht leer, nicht nur Leerzeichen |
| `amount` | Integer oder Float | Positiv, endlich; kein String oder `bool` |
| `unit` | String | Exakt `g`, `ml` oder `Stück` |

Beispiel für eine gültige Importdatei (`data/import_tomatensuppe.json`):

```json
{
    "name": "Tomatensuppe",
    "portions": 4,
    "ingredients": [
        {"name": "Tomaten", "amount": 500.0, "unit": "g"},
        {"name": "Wasser", "amount": 300.0, "unit": "ml"}
    ]
}
```

### Verarbeitung

1. `main.py` nimmt über Menüpunkt 2 einen Dateipfad entgegen und ruft `import_new_recipe(file_path)` auf.
2. `import_new_recipe(file_path)` befindet sich in **`recipe_input.py`**. Es lädt zuerst die bestehende Rezeptliste mit `load_recipes()`.
3. `import_recipe(file_path)` in `storage.py` öffnet die angegebene JSON-Datei und liest sie mit `json.load()` ein.
4. `validate_import_recipe(recipe)` in `validation.py` überprüft die Struktur, die Pflichtfelder und sämtliche Zutaten. Bei einem ungültigen Rezept gibt `import_recipe()` `None` zurück.
5. Bei gültigen Daten übernimmt `import_new_recipe()` auf Rezept-Ebene nur `name`, `portions` und `ingredients` in ein neues Dictionary `clean_recipe`.
6. `add_recipe_id()` vergibt eine neue ID. Die Standardfelder `favorite = False` und `allergies = []` werden unabhängig von eventuellen zusätzlichen Importfeldern gesetzt.
7. Die neue Version wird an die bestehende Liste angehängt und mit `save_recipes(recipes)` gespeichert.

**Abgrenzung:** Nicht vorgesehene Felder auf Rezept-Ebene (z. B. `description`) werden nicht mitgespeichert. Die vorhandenen Zutaten-Dictionaries werden hingegen als Liste übernommen und nicht zusätzlich auf unerwartete Schlüssel bereinigt. Die über `ask_recipe_allergies()` gewählten Allergien betreffen ausschliesslich die manuelle Eingabe, nicht den JSON-Import.

### Fehlerbehandlung

- Fehlende Importdatei (`FileNotFoundError`): Meldung „Die Datei wurde nicht gefunden.“, Rückgabe `None`.
- Beschädigtes Import-JSON (`json.JSONDecodeError`): Meldung „Die Importdatei ist beschädigt.“, Rückgabe `None`.
- Gültiges JSON, aber ungültige Rezeptdaten: Meldung „Das Rezept enthält ungültige Daten.“, Rückgabe `None`.
- Ist der Import ungültig, beendet `import_new_recipe()` den Vorgang ohne `save_recipes()` aufzurufen. Bestehende Rezepte bleiben unverändert.
- Beschädigte gespeicherte Daten in `data/recipes.json` werden von `load_recipes()` mit `raise` gemeldet, damit sie nicht überschrieben werden.
- Über `import_recipe()` steht ein `#`-Kommentar, der auf die Entstehung der Funktion im Rahmen des Feedbacks von Dr. Härer verweist.

### Durchgeführte Tests

- Gültige Importdatei erfolgreich eingelesen und gespeichert.
- Ungültige Rezeptwerte, fehlende Pflichtfelder und fehlerhafte Zutaten abgelehnt.
- Fehlende Datei und beschädigtes Import-JSON mit passenden Meldungen behandelt.
- Zwei Rezepte nacheinander importiert; das erste blieb erhalten und die IDs unterschieden sich.
- Ungültiger Import veränderte die vorhandene Rezeptliste nicht.
- Zusätzliche Felder auf Rezept-Ebene wurden beim Speichern ignoriert, eine mitgelieferte ID wurde ersetzt.
- Die zusätzliche Meldung bei ungültigen Rezeptdaten wurde getestet.

## US08 – Nach Zutaten und Allergien filtern

### Beschreibung

Die Filterfunktionen können Rezepte nach Zutaten suchen und Rezepte mit bestimmten Allergien ausschliessen. Die beiden Filter werden unabhängig voneinander verwendet.

### Funktionen (`recipe_features.py`)

| Funktion | Aufgabe |
|---|---|
| `input_ingredients()` | Suchzutaten nacheinander bis `fertig` erfassen; mindestens eine Zutat nötig; Rückgabe als Liste in Kleinbuchstaben |
| `ingredient_filter()` | Rezepte finden, die alle eingegebenen Zutaten enthalten; Namen der Treffer ausgeben und Trefferliste zurückgeben |
| `user_input_allergies()` | Allergienamen für den **Filter** als Text erfassen; Abschluss mit `fertig` erst nach mindestens einer Auswahl; Rückgabe als Liste |
| `allergies_filter()` | Rezepte ausschliessen, die eine der angegebenen Allergien enthalten; Namen der übrigen Rezepte ausgeben und Liste zurückgeben |

### Ablauf Zutatenfilter

1. `input_ingredients()` fragt wiederholt nach Suchzutaten und normalisiert jede Eingabe mit `strip()` und `lower()`.
2. Leere Eingaben werden mit einer Meldung abgelehnt. `fertig` beendet die Eingabe nur, wenn bereits mindestens eine Zutat erfasst wurde.
3. `ingredient_filter()` lädt die Rezepte mit `load_recipes()` und erstellt pro Rezept eine Liste der Zutatennamen in Kleinbuchstaben.
4. Ein Rezept passt nur, wenn **jede** Suchzutat in dieser Liste vorkommt. Sobald eine Zutat fehlt, wird die Prüfung für dieses Rezept mit `break` abgebrochen.
5. Ausgabe bei Treffern: `Das sind die Rezepte, die deinen Suchkriterien entsprechen: …`; ohne Treffer: `Es wurden keine Rezepte gefunden.`

### Ablauf Allergiefilter

1. `user_input_allergies()` zeigt zuerst alle möglichen Allergien an (`Gluten`, `Laktose`, `Nüsse`, `Eier`, `Soja`, `Sesam`, `Krebstiere`, `Weichtiere`).
2. Der Benutzer gibt Allergien **als Text** ein, anders als bei der nummerierten Auswahl in `ask_recipe_allergies()`. Gross-/Kleinschreibung und Leerzeichen am Rand werden ignoriert; gespeichert wird die Schreibweise mit grossem Anfangsbuchstaben (z. B. `laktose` → `Laktose`).
3. Ungültige Eingaben werden mit einer eigenen Meldung abgelehnt: leere Eingabe, bereits erfasste Allergie und Allergie, die nicht in der Liste steht.
4. `fertig` beendet die Eingabe nur, wenn mindestens eine Allergie erfasst wurde.
5. `allergies_filter()` lädt die Rezepte und übernimmt nur Rezepte, deren Feld `allergies` keine der eingegebenen Allergien enthält.
6. Ausgabe bei Treffern: `Diese Rezepte enthalten keine deiner angegebenen Allergien: …`; ohne Treffer: `Es wurden keine Rezepte ohne diese Allergien gefunden.`

### Dokumentierte manuelle Prüfungen

- Einzelne und mehrere Suchzutaten; fehlende Treffer.
- Vergleich ohne Beachtung der Gross-/Kleinschreibung bei Zutatennamen.
- Abweisen leerer Suchbegriffe; `fertig` ohne Suchzutat ist nicht zulässig.

**Hinweis:** Für den Allergiefilter sind in dieser Dokumentation noch keine manuellen Tests festgehalten.

## US11 – Favoriten

### Beschreibung

Benutzer können Rezepte als Favoriten markieren, die Markierung entfernen und eine Übersicht über Favoriten abrufen. Das Datenmodell verwendet dafür das Feld `favorite` (`bool`). Die Funktionen sind in `recipe_features.py` umgesetzt.

### Funktionen (`recipe_features.py`)

| Funktion | Aufgabe |
|---|---|
| `edit_favorites()` | Einstiegspunkt der Favoritenverwaltung: fragt, ob Favoriten angezeigt oder bearbeitet werden sollen; beim Bearbeiten Aktion durchführen und speichern |
| `get_favorites()` | Rezepte mit `favorite = True` sammeln, Namen ausgeben und Liste zurückgeben |
| `user_input1_favorites()` | Vorhandene Rezept-ID abfragen; nur Zahlen akzeptieren, die als ID existieren |
| `user_input2_favorites()` | Aktion `hinzufügen` oder `entfernen` abfragen |

### Ablauf `edit_favorites()`

1. Der Benutzer wird gefragt: `1 = Favoriten anzeigen, 2 = Favoriten bearbeiten (Bitte Zahl 1 oder 2 angeben): `.
2. Bei jeder anderen Eingabe als `2` wird `get_favorites()` aufgerufen. Diese Funktion gibt `Diese Rezepte sind deine Favoriten: …` oder `Du hast keine Favoriten gespeichert.` aus.
3. Bei `2` werden alle gespeicherten Rezepte mit Name, ID und Favoritenstatus angezeigt.
4. `user_input1_favorites()` fragt so lange nach, bis eine existierende Rezept-ID eingegeben wird.
5. `user_input2_favorites()` fragt so lange nach, bis `hinzufügen` oder `entfernen` eingegeben wird (unabhängig von Gross-/Kleinschreibung und Leerzeichen).
6. Beim gewählten Rezept wird `favorite` auf `True` bzw. `False` gesetzt und eine Bestätigung ausgegeben.
7. Die Rezeptliste wird mit `save_recipes()` in `data/recipes.json` gespeichert.

### Bisher in der Dokumentation festgehaltene manuelle Tests

- Ein Rezept als Favorit markieren und die Markierung entfernen.
- Ungültige IDs und Aktionen ablehnen.
- Übersicht mit und ohne Favoriten anzeigen.

**Status:** Die Funktionen sind implementiert.

## Allergien – in US01 integriert (zuvor US12)

### Beschreibung und Entscheidung nach Dozentenfeedback

Die Zuordnung von Allergien ist **keine separat zu implementierende User Story mehr**. Sie ist Bestandteil der manuellen Rezepterfassung (US01). Die Funktion `ask_recipe_allergies()` stammt aus der von Mai vorbereiteten Lösung und wurde in `recipe_input.ask_recipe()` eingebunden.

Die bisherige Beschreibung einer nachträglichen Allergiebearbeitung über `edit_allergies()` und `user_input1_allergies()`/`user_input2_allergies()` entsprach **nicht** dem hochgeladenen Python-Code: Diese Funktionen sind darin nicht vorhanden. Sie werden deshalb hier nicht als implementiert geführt.

### Auswahlliste und Eingabe bei US01

In `recipe_features.py` ist folgende feste Liste definiert: `Gluten`, `Laktose`, `Nüsse`, `Eier`, `Soja`, `Sesam`, `Krebstiere`, `Weichtiere`.

1. `ask_recipe_allergies()` zeigt die Allergien mit den Nummern 1 bis 8 an.
2. Der Benutzer wählt über `Allergie auswählen (1-8 oder fertig): ` eine Nummer aus.
3. Die gewählte Allergie wird der Rückgabeliste hinzugefügt, wenn sie noch nicht vorhanden ist. Ungültige und doppelte Nummern lösen eine Meldung aus.
4. `fertig` beendet die Auswahl – auch wenn keine Allergie gewählt wurde.
5. `ask_recipe()` speichert die Rückgabeliste im Rezept-Dictionary unter `allergies`.
6. `create_recipe()` speichert das Rezept und gibt die gewählten Allergien unter der Überschrift `Allergien:` einzeln aus.

### Abgrenzung zum Allergiefilter

`user_input_allergies()` und `allergies_filter()` bleiben als eigenständige **Filterfunktionen** in `recipe_features.py` bestehen. Sie nehmen Allergienamen als Text entgegen und suchen Rezepte, die diese Allergien *nicht* enthalten. Sie werden nicht für die Allergiezuordnung während der Rezepterfassung verwendet.

### Durchgeführte manuelle Tests

- Auswahl der Allergien `1` und `3` und Abschluss mit `fertig` → `['Gluten', 'Nüsse']`.
- Übernahme der Auswahl in das von `ask_recipe()` erzeugte Dictionary.
- Persistenz der ausgewählten Allergien in `data/recipes.json` nach `create_recipe()`.
- Übersichtliche Ausgabe der Allergien nach der Rezepterfassung.

**Noch offen:** Eine nachträgliche Allergiebearbeitung ist in diesem Code-Stand nicht umgesetzt. Sie ist nach der geänderten Anforderung kein eigener Teil des aktuellen US01-Erfassungsablaufs.

## 9. Dozentenfeedback – umgesetzte Änderungen

Die Änderungen wurden auf dem Korrektur-Branch entwickelt und betreffen die Benutzerführung und die Modulaufteilung:

| Rückmeldung | Umsetzung im Code |
|---|---|
| Eingaben als Aufforderungen, mit Abstand zur Eingabe | Sechs `input()`-Texte in `recipe_input.py` angepasst; auch `ask_recipe_allergies()` verwendet die Form `Allergie auswählen (1-8 oder fertig): ` |
| Anmerkung bei der Importfunktion | Zwei `#`-Kommentarzeilen unmittelbar vor `import_recipe()` in `storage.py` mit Verweis auf Dr. Härer |
| Rezept nicht als Dictionary ausgeben | `create_recipe()` gibt Name, Portionen, Zutaten und ausgewählte Allergien mit `print()` und f-Strings aus |
| Allergien in die Rezepterfassung aufnehmen | `ask_recipe_allergies()` aus `recipe_features.py` wird in `recipe_input.ask_recipe()` aufgerufen; die Liste wird unter `allergies` gespeichert |

**Zusätzliche Moduländerung:** `create_recipe()` und `import_new_recipe()` wurden aus `main.py` nach `recipe_input.py` verschoben. Das Hauptmenü importiert sie und ruft sie über die Optionen 1 und 2 auf.

**Abgrenzung:** Das Dozentenfeedback wurde gezielt an den oben genannten Stellen umgesetzt. Andere Eingabeaufforderungen und Anzeigen, insbesondere in nicht damit verbundenen Team-Modulen und teilweise in `main.py`, sind noch nicht einheitlich überarbeitet.

## 10. Weitere Entwicklungsschritte

1. **Integration:** Vorhandene Funktionen für Rezeptdetails (`recipe_display.py`), Löschen (`recipe_delete.py`), Zutaten-/Allergiefilter und Favoriten in die entsprechenden Menüoptionen von `main.py` einbinden. Bearbeiten ist im hochgeladenen Stand noch ein Platzhalter.
2. **Qualitätssicherung:** Weitere Dateifehler, gültiges JSON mit unerwarteter Struktur in `data/recipes.json` und gruppenübergreifende Integrationstests bearbeiten. Bisherige Tests waren überwiegend manuell.
3. **Dokumentation:** Funktionsbaum, Verantwortlichkeiten und Kontrollfluss bei neuen Entwicklungen weiter abgleichen, insbesondere nach Team-Merges und Änderungen an User Storys.
