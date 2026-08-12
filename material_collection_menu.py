from Materials import (
    find_materials_at_location,
    add_found_material_to_inventory,
    add_all_found_materials_to_inventory,
)
from terminal_ui import (
    show_invalid_input,
    show_no_visible_materials,
    show_no_materials_found,
    ask_material_choice,
    show_materials_collected,
    show_material_collected,
    show_material_choice_hint,
)


def open_material_collection(professor, current_location):
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