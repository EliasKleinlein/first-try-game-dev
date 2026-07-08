from materials import get_random_find_amount, material_can_be_found
from inventory_ui import show_inventory
from navigation import get_available_directions, get_location_id_for_direction
from terminal_ui import (
    show_environment_details,
    show_status,
    show_placeholder,
    show_invalid_input,
    show_game_ended,
    ask_direction_choice,
)


def examine_environment(current_location):
    show_environment_details(current_location)


def choose_direction(current_location):
    directions = get_available_directions(current_location)
    direction_index = ask_direction_choice(directions)

    if direction_index is None:
        return None

    return get_location_id_for_direction(current_location, direction_index)


def collect_material(professor, current_location):
    if not current_location.visible_materials:
        print("\nHier ist aktuell kein brauchbares Material sichtbar.")
        return

    materials = current_location.visible_materials

    found_materials = []

    for material in materials:
        if material_can_be_found(material):
            amount = get_random_find_amount(material)
            found_materials.append((material, amount))

    if not found_materials:
        print("\nDu suchst die Umgebung ab, findest aber nichts Brauchbares.")
        return

    print("\nWelches Material möchtest du aufnehmen?")

    for index, material_data in enumerate(found_materials, start=1):
        material_name = material_data[0]
        amount = material_data[1]
        print(f"[{index}] {material_name}: {amount}x")

    print("[a] Alles nehmen")
    print("[0] Zurück")

    choice = input("Eingabe: ")

    if choice == "0":
        return

    if choice.lower() == "a":
        print()

        for material_name, amount in found_materials:
            professor.add_material(material_name, amount)
            print(f"{material_name} aufgenommen: {amount}x")

        print("\nAlle aufgenommenen Materialien wurden als entdeckt markiert.")
        return

    if not choice.isdigit():
        print("\nUngültige Eingabe.")
        return

    choice_index = int(choice) - 1

    if choice_index < 0 or choice_index >= len(found_materials):
        print("\nUngültige Eingabe.")
        return

    selected_material, amount = found_materials[choice_index]
    professor.add_material(selected_material, amount)

    print(f"\n{selected_material} wurde aufgenommen: {amount}x")
    print(f"{selected_material} wurde als entdeckt markiert.")
    return


def handle_choice(choice, state):
    professor = state.professor
    current_location = state.current_location()
    current_location_id = state.current_location_id
    if choice == "1":
        examine_environment(current_location)

        new_location_id = choose_direction(current_location)

        if new_location_id is not None:
            current_location_id = new_location_id
    elif choice == "2":
        collect_material(professor, current_location)
    elif choice == "3":
        show_inventory(professor)
    elif choice == "4":
        show_placeholder("Forschungsmenü ist noch nicht implementiert.")
    elif choice == "5":
        show_placeholder("Baumenü ist noch nicht implementiert.")
    elif choice == "6":
        show_status(professor)
    elif choice == "0":
        show_game_ended()
        state.running = False
    else:
        show_invalid_input()

    return current_location_id