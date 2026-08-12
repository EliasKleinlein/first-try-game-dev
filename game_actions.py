from inventory_ui import show_inventory
from navigation import get_available_directions, get_location_id_for_direction
from research_menu import open_research_menu
from material_collection_menu import open_material_collection
from terminal_ui import (
    show_environment_details,
    show_status,
    show_placeholder,
    show_invalid_input,
    show_game_ended,
    ask_direction_choice,
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
        open_material_collection(professor, current_location)
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