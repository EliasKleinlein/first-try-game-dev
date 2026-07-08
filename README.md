# Professor Prototype

## Projektbeschreibung

**Professor Prototype** ist ein textbasierter Survival-, Forschungs- und Aufbauspiel-Prototyp.

Der Spieler übernimmt einen Professor, der ca. 3700 Jahre nach einem unbekannten Phänomen erwacht. Dieses Phänomen hat die Menschheit versteinert. Der Professor macht es sich zur Aufgabe, die Ursache der Versteinerung herauszufinden und die Zivilisation Schritt für Schritt durch Wissen, Experimente, Werkzeuge und Aufbau zurückzubringen.

## Grundidee

Der Professor besitzt theoretisches Wissen, kann es aber zu Beginn nicht praktisch anwenden. Ihm fehlen Werkzeuge, Equipment, Labor, Infrastruktur und körperliche Stärke.

Fortschritt entsteht daher nicht durch rohe Kraft, sondern durch:

- Beobachten
- Sammeln
- logisches Kombinieren
- Experimentieren
- Werkzeugbau
- Forschung
- Ausbau der Umgebung

## Core Loop

Umgebung untersuchen
→ Materialien finden
→ Materialien ins Inventar aufnehmen
→ Materialien als entdeckt markieren
→ Materialien untersuchen
→ Eigenschaften erkennen
→ Werkzeuge / Prozesse freischalten
→ neue Möglichkeiten erhalten

## Story-Start

Der Professor erwacht in einer Höhle. In der Höhle riecht es nach Salpetersäure. Nachdem er die Höhle verlässt, steht er auf einer Lichtung.

Seine ersten Prioritäten:

1. Wasser finden
2. Schutz sichern
3. Feuer ermöglichen
4. primitive Werkzeuge herstellen
5. wissenschaftliche Grundlagen praktisch nutzbar machen

## Charakter

Startwerte des Professors:

| Wert           | Startwert |
| -------------- | --------: |
| Gesundheit     |      100% |
| Wasserhaushalt |  variabel |
| Sättigung      |      100% |
| Ausdauer       |        20 |
| Kraft          |        10 |
| IQ             |  Legendär |

Besonderheiten:

- Der Professor ist hochintelligent.
- Er ist körperlich eingeschränkt.
- Sein IQ wird als **Legendär** angezeigt.
- Spätere Charaktere sollen IQ-Werte als Zahlen erhalten.

## Tages- und Nachtzyklus

| Parameter              | Wert             |
| ---------------------- | ---------------- |
| Spielstart             | Tag 1, 09:33 Uhr |
| Tag                    | 08:00–22:00      |
| Nacht                  | 22:00–08:00      |
| Tagdauer in Echtzeit   | 20 Minuten       |
| Nachtdauer in Echtzeit | 5 Minuten        |

Der Timer läuft automatisch und unabhängig von Spieleraktionen.

### Nachtlogik

- Beim Wechsel in die Nacht wird der Spieler gewarnt.
- Ohne Licht ist der Professor nachts handlungsunfähig.
- Der Spieler kann die Nacht überspringen.
- Wer nachts draußen bleibt, wird von einem zufälligen Raubtier angegriffen.
- Nach GAME OVER springt das Spiel automatisch zum nächsten Morgen.

## Orte

Aktuell definierte Orte:

### Höhle

- dunkler, feuchter Ort
- Geruch nach Salpetersäure
- führt zur Lichtung

### Lichtung vor der Höhle

Sichtbare Materialien:

- Stock
- Stein
- Laub

Wege:

- zurück zur Höhle
- links zum Bach
- rechts Richtung Meer
- geradeaus in den Wald

### Weitere Platzhalter-Orte

- Bachlauf
- Blick Richtung Meer
- Waldrand

## Materialien

Aktuelle Anfangsmaterialien:

- Stock
- Stein
- Harter Stein
- Splitternder Stein
- Weicher Stein
- Weichholz
- Hartholz
- Laub
- Großes Palmenblatt
- Bambusreste
- Bambusstange

Materialien besitzen Eigenschaften, die nicht immer sofort bekannt sind. Diese Eigenschaften sollen später durch Experimente erforscht werden.

Beispiele:

- Stein gegen Stein schlagen
- Holzstruktur untersuchen
- Bambusreste auswerten

## Raritäten

| Rarität      | Fundwahrscheinlichkeit |
| ------------ | ---------------------: |
| Primitiv     |                    80% |
| Gewöhnlich   |                    60% |
| Ungewöhnlich |                    35% |
| Selten       |                    15% |
| Episch       |                     7% |
| Legendär     |                     3% |

## Inventar

Das Inventar speichert Materialien mit Mengenangaben.

Stapelregel:

Maximal 100 Items pro Stapel

Beispiel:

Laub: 100x
Laub: 20x

## Aktuelle Projektdateien

game_menu.py # Hauptmenü, Intro, Navigation
character.py # Charakterwerte und Inventar
game_time.py # automatischer Tages-/Nachtzyklus
materials.py # Materialien, Raritäten, Fundmengen
locations.py # Orte und Wege
README.md # Projektübersicht

## Technischer Ansatz

Das Projekt nutzt datengetriebenes Design.

Code definiert Systeme.
Daten definieren Inhalte.

Materialien, Orte und spätere Reaktionen sollen möglichst als Daten erweitert werden, ohne den Kerncode ständig umzubauen.

## Aktueller Entwicklungsfokus

Der aktuelle Fokus liegt auf:

- Umgebung untersuchen
- Orte und Wege
- Materialfunde
- Inventar mit Mengen und Stapeln
- Vorbereitung des Forschungssystems
