import time

from story import (
    GAME_TITLE,
    INTRO_TEXT,
    PROFESSOR_START_THOUGHTS,
    NIGHT_WARNING_TEXT,
    NIGHT_STAY_OUTSIDE_TEXT,
    GAME_OVER_NIGHT_TEXT,
)


def typewriter_text(text, delay=0.03):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def show_intro():
    skip = input("Intro ansehen? [Enter = ja / s = überspringen]: ")

    if skip.lower() == "s":
        return

    for line in INTRO_TEXT:
        typewriter_text(line)
        time.sleep(0.5)

    input("\nJunger Professor, bist du der Aufgabe gewachsen? Dann drücke jetzt Enter...")


def show_layout(professor, game_time, current_location):
    print("=" * 50)
    print(f"              {GAME_TITLE.upper()}")
    print("=" * 50)
    print()
    print(f"NAME: {professor.name}")
    print(f"ZEIT: {game_time.display()}")
    print(f"LEBEN: {professor.life_percent()}%")
    print(f"WASSERHAUSHALT: {professor.thirst_percent()}%")
    print(f"SÄTTIGUNG: {professor.hunger_percent()}%")
    print(f"KRAFT/AUSDAUER: {professor.strength_stamina_display()}")
    print(f"IQ: {professor.iq_display()}")
    print()
    print("-" * 50)
    print("GEDANKEN")
    print("-" * 50)

    for thought in PROFESSOR_START_THOUGHTS:
        print(f'"{thought}"')

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
    print("-" * 50)
    print("AKTUELLER ORT")
    print("-" * 50)
    print(f"ORT: {current_location.name}")
    print(current_location.description)
    print()

def ask_skip_night():
    print()

    for line in NIGHT_WARNING_TEXT:
        print(line)

    return input("Nacht überspringen? [j = schlafen / n = draußen bleiben]: ")


def show_night_game_over(predator):
    print()

    for line in NIGHT_STAY_OUTSIDE_TEXT:
        print(line)

    print(f"Ein {predator} greift dich an.")
    print("Ohne Licht, Schutz oder Orientierung hast du keine Chance.")

    print("\n" + "=" * 50)
    print(f"                    {GAME_OVER_NIGHT_TEXT[0]}")
    print("=" * 50)
    print(GAME_OVER_NIGHT_TEXT[1])
    print("=" * 50)

    input("\nDrücke Enter, um am nächsten Morgen neu zu erwachen...")
    
def ask_player_name():
    return input(
        "\nJunger Professor, wie ist dein Name?\n"
        "Gib deinen Namen hier ein: "
    )
    
def ask_menu_choice():
    return input("Eingabe: ")

def wait_for_continue():
    input("\nDrücke Enter, um fortzufahren...")
    
def show_environment_details(current_location):
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


def show_placeholder(message):
    print(f"\n{message}")


def show_invalid_input():
    print("\nUngültige Eingabe.")


def show_game_ended():
    print("\nSpiel beendet.")
    
def ask_direction_choice(directions):
    if not directions:
        print("\nEs gibt keinen erkennbaren Weg von hier.")
        return None

    print("\nWohin möchtest du gehen?")

    for index, direction in enumerate(directions, start=1):
        print(f"[{index}] {direction}")

    print("[0] Bleiben")

    choice = input("Eingabe: ")

    if choice == "0":
        return None

    if not choice.isdigit():
        return -1

    return int(choice) - 1

def show_no_visible_materials():
    print("\nHier ist aktuell kein brauchbares Material sichtbar.")


def show_no_materials_found():
    print("\nDu suchst die Umgebung ab, findest aber nichts Brauchbares.")


def ask_material_choice(found_materials):
    print("\nWelches Material möchtest du aufnehmen?")

    for index, material_data in enumerate(found_materials, start=1):
        material_name = material_data[0]
        amount = material_data[1]
        print(f"[{index}] {material_name}: {amount}x")

    print("[a] Alles nehmen")
    print("[0] Zurück")

    return input("Eingabe: ")


def show_materials_collected(found_materials):
    print()

    for material_name, amount in found_materials:
        print(f"{material_name} aufgenommen: {amount}x")

    print("\nAlle aufgenommenen Materialien wurden als entdeckt markiert.")


def show_material_collected(material_name, amount):
    print(f"\n{material_name} wurde aufgenommen: {amount}x")
    print(f"{material_name} wurde als entdeckt markiert.")
    
def show_material_choice_hint():
    print("Gültige Eingaben: Zahl des Materials, a = alles nehmen, 0 = zurück.")
    
def show_direction_choice_hint():
    print("Gültige Eingaben: Zahl der Richtung, 0 = bleiben.")

def show_research_menu():
    print("\n" + "-" * 50)
    print("FORSCHUNG / HYPOTHESEN")
    print("-" * 50)
    print("[1] Periodensystem")
    print("[2] Entdeckte Materialien")
    print("[3] Forschen")
    print("[4] Experimente")
    print("[5] Hypothesen")
    print("[0] Zurück")
    print()


def ask_research_choice():
    return input("Eingabe: ")