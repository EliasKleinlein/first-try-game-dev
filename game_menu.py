import time
import random
from character import Character
from game_time import GameTime
from locations import LOCATIONS



def typewriter_text(text, delay=0.03):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def show_intro():
    skip = input("Intro ansehen? [Enter = ja / s = überspringen]: ")

    if skip.lower() == "s":
        return

    intro_text = [
        "Vor etwa 3700 Jahren ereignete sich ein unbekanntes Phänomen.",
        "Innerhalb kürzester Zeit wurde die gesamte Menschheit versteinert.",
        "Städte verstummten. Maschinen kamen zum Stillstand.",
        "Die Welt ging weiter. Ohne den Menschen.",
        "",
        "Nach 3700 Jahren erwacht ein einzelner Mensch.",
        "Ein Professor.",
        "",
        "Er weiß nicht, warum er erwacht ist.",
        "Doch er macht es sich zur Aufgabe, die Ursache der Versteinerung herauszufinden.",
        "Und die Zivilisation Schritt für Schritt zurückzubringen.",
    ]

    for line in intro_text:
        typewriter_text(line)
        time.sleep(0.5)

    input("\nJunger Professor, bist du der Aufgabe gewachsen? Dann drücke jetzt Enter...")


def show_layout(professor, game_time, current_location):
    print("=" * 50)
    print("              PROFESSOR PROTOTYPE")
    print("=" * 50)
    print()
    print(f"ORT: {current_location.name}")
    print(current_location.description)
    print(f"ZEIT: {game_time.display()}")
    print("ZUSTAND: erwacht | durstig | nackt | ohne Schutz | ohne Werkzeug")
    print()
    print(f"NAME: {professor.name}")
    print(f"LEBEN: {professor.life_percent()}%")
    print(f"DURST: {professor.thirst_percent()}%")
    print(f"HUNGER: {professor.hunger_percent()}%")
    print(f"KRAFT/AUSDAUER: {professor.strength_stamina_display()}")
    print(f"IQ: {professor.iq_display()}")
    print()
    print("-" * 50)
    print("GEDANKEN")
    print("-" * 50)
    print('"Was ist geschehen? Wo bin ich? Wie viel Zeit ist vergangen?"')
    print('"Priorität: Wasser. Danach Schutz. Dann Feuer."')
    print()
    print("-" * 50)
    print("AKTIONEN")
    print("-" * 50)
    print("[1] Umgebung untersuchen")
    print("[2] Material sammeln")
    print("[3] Inventar ansehen")
    print("[4] Forschung / Hypothesen")
    print("[5] Bauen / Herstellen")
    print("[6] Status ansehen")
    print("[0] Spiel beenden")
    print()

def examine_environment(current_location):
    print("\n" + "-" * 50)
    print("UMGEBUNG UNTERSUCHEN")
    print("-" * 50)
    print(f"Ort: {current_location.name}")
    print(current_location.description)

    if current_location.smells:
        print("\nGerüche:")
        for smell in current_location.smells:
            print(f"- {smell}")

    if current_location.sounds:
        print("\nGeräusche:")
        for sound in current_location.sounds:
            print(f"- {sound}")

    if current_location.visible_materials:
        print("\nSichtbare Materialien:")
        for material in current_location.visible_materials:
            print(f"- {material}")

    if current_location.exits:
        print("\nMögliche Wege:")
        for direction in current_location.exits:
            print(f"- {direction}")

    print("-" * 50)

def choose_direction(current_location):
    if not current_location.exits:
        print("\nEs gibt keinen erkennbaren Weg von hier.")
        return None

    directions = list(current_location.exits.keys())

    print("\nWohin möchtest du gehen?")

    for index, direction in enumerate(directions, start=1):
        print(f"[{index}] {direction}")

    print("[0] Zurück")

    choice = input("Eingabe: ")

    if choice == "0":
        return None

    if not choice.isdigit():
        print("\nUngültige Eingabe.")
        return None

    choice_index = int(choice) - 1

    if choice_index < 0 or choice_index >= len(directions):
        print("\nUngültige Eingabe.")
        return None

    selected_direction = directions[choice_index]
    return current_location.exits[selected_direction]

def show_status(professor):
    print("\n" + "-" * 50)
    print("STATUS")
    print("-" * 50)
    print(f"Name: {professor.name}")
    print(f"Gesundheit: {professor.life_percent()}%")
    print(f"Wasserhaushalt: {professor.thirst_percent()}%")
    print(f"Sättigung: {professor.hunger_percent()}%")
    print(f"Kraft/Ausdauer: {professor.strength_stamina_display()}")
    print(f"IQ: {professor.iq_display()}")
    print("-" * 50)

def handle_choice(choice, professor, current_location, current_location_id):
    if choice == "1":
        examine_environment(current_location)

        new_location_id = choose_direction(current_location)

        if new_location_id is not None:
            current_location_id = new_location_id
    elif choice == "2":
        print("\nDu suchst nach brauchbaren Materialien.")
    elif choice == "3":
        print("\nInventar ist noch leer.")
    elif choice == "4":
        print("\nForschungsmenü ist noch nicht implementiert.")
    elif choice == "5":
        print("\nBaumenü ist noch nicht implementiert.")
    elif choice == "6":
        show_status(professor)
    elif choice == "0":
        print("\nSpiel beendet.")
    else:
        print("\nUngültige Eingabe.")
    return current_location_id

def main():
    show_intro()

    player_name = input(
        "\nJunger Professor, wie ist dein Name?\n"
        "Gib deinen Namen hier ein: "
    )

    professor = Character(name=player_name)
    game_time = GameTime()
    current_location_id = "cave"

    running = True

    while running:
        game_time.update()

        if game_time.just_entered_night():
            print("\nEs wird Nacht.")
            print("Ohne Licht bist du bis zum Morgen handlungsunfähig.")
            print("Wenn du trotzdem draußen bleibst, riskierst du, von einem wilden Tier gefressen zu werden.")

            skip = input("Nacht überspringen? [j = schlafen / n = draußen bleiben]: ")

            if skip.lower() == "j":
                game_time.skip_night()
            else:
                predator = random.choice(["Löwe", "Tiger", "Wolf", "Bär", "Raubtier"])

                print("\nDu bleibst trotz völliger Dunkelheit draußen.")
                print("Etwas bewegt sich zwischen den Bäumen...")
                print(f"Ein {predator} greift dich an.")
                print("Ohne Licht, Schutz oder Orientierung hast du keine Chance.")

                print("\n" + "=" * 50)
                print("                    GAME OVER")
                print("=" * 50)
                print("Du wurdest in der Nacht von einem wilden Tier getötet.")
                print("=" * 50)

                input("\nDrücke Enter, um am nächsten Morgen neu zu erwachen...")

                professor.reset_after_game_over()
                game_time.skip_night()

        current_location = LOCATIONS[current_location_id]
        show_layout(professor, game_time, current_location)

        choice = input("Eingabe: ")

        if choice == "0":
            current_location_id = handle_choice(choice, professor, current_location, current_location_id)
            running = False
        else:
            current_location_id = handle_choice(choice, professor, current_location, current_location_id)
            input("\nDrücke Enter, um fortzufahren...")


main()