from Materials import (
    find_materials_at_location,
    add_found_material_to_inventory,
    add_all_found_materials_to_inventory,
)
from inventory_ui import show_inventory
from navigation import get_available_directions, get_location_id_for_direction
from research_menu import open_research_menu
from terminal_ui import (
    show_environment_details,
    show_status,
    show_placeholder,
    show_invalid_input,
    show_game_ended,
    ask_direction_choice,
    show_no_visible_materials,
    show_no_materials_found,
    ask_material_choice,
    show_materials_collected,
    show_material_collected,
    show_material_choice_hint,
    show_direction_choice_hint,
)


def examine_environment(current_location):
    show_environment_details(current_location)


def choose_direction(current_location):
    directions = get_available_directions(current_location)

    while True:
        direction_index = ask_direction_choice(directions)

        if direction_index is None:
            return None

        if direction_index == -1:
            show_invalid_input()
            show_direction_choice_hint()
            continue

        new_location_id = get_location_id_for_direction(current_location, direction_index)

        if new_location_id is None:
            show_invalid_input()
            show_direction_choice_hint()
            continue

        return new_location_id


def collect_material(professor, current_location):
    if not current_location.visible_materials:
        show_no_visible_materials()
        return

    found_materials = find_materials_at_location(current_location)

    if not found_materials:
        show_no_materials_found()
        return

    while True:
        choice = ask_material_choice(found_materials)

        if choice == "0":
            return

        if choice.lower() == "a":
            add_all_found_materials_to_inventory(professor, found_materials)
            show_materials_collected(found_materials)
            return

        if not choice.isdigit():
            show_invalid_input()
            show_material_choice_hint()
            continue

        choice_index = int(choice) - 1

        if choice_index < 0 or choice_index >= len(found_materials):
            show_invalid_input()
            show_material_choice_hint()
            continue

        selected_material, amount = found_materials[choice_index]
        add_found_material_to_inventory(professor, selected_material, amount)

        show_material_collected(selected_material, amount)
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
        open_research_menu()
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