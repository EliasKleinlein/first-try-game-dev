import time
from character import Character


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


def show_layout(professor):
    print("=" * 50)
    print("              PROFESSOR PROTOTYPE")
    print("=" * 50)
    print()
    print("ORT: Unbekannt")
    print("ZUSTAND: erwacht | durstig | nackt | ohne Schutz | ohne Werkzeug")
    print()
    print(f"NAME: {professor.name}")
    print(f"LEBEN: {professor.life_percent()}%")
    print(f"DURST: {professor.thirst_percent()}%")
    print(f"HUNGER: {professor.hunger_percent()}%")
    print(f"KRAFT/AUSDAUER: {professor.strength_stamina_display()}")
    print(f"IQ: {professor.iq}")
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


def handle_choice(choice):
    if choice == "1":
        print("\nDu untersuchst vorsichtig die Umgebung.")
    elif choice == "2":
        print("\nDu suchst nach brauchbaren Materialien.")
    elif choice == "3":
        print("\nInventar ist noch leer.")
    elif choice == "4":
        print("\nForschungsmenü ist noch nicht implementiert.")
    elif choice == "5":
        print("\nBaumenü ist noch nicht implementiert.")
    elif choice == "6":
        print("\nStatus: durstig, nackt, ohne Schutz, ohne Werkzeug.")
    elif choice == "0":
        print("\nSpiel beendet.")
    else:
        print("\nUngültige Eingabe.")


def main():
    show_intro()
    player_name = input(
        "\nJunger Professor, wie ist dein Name?\n"
        "Gib deinen Namen hier ein: "
    )
    professor = Character(name=player_name)
    
    running = True

    while running:
        show_layout(professor)
        choice = input("Eingabe: ")

        if choice == "0":
            handle_choice(choice)
            running = False
        else:
            handle_choice(choice)
            input("\nDrücke Enter, um fortzufahren...")


main()
