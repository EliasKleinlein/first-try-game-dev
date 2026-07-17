from Materials import get_random_find_amount, material_can_be_found


def find_materials_at_location(current_location):
    found_materials = []

    for material in current_location.visible_materials:
        if material_can_be_found(material):
            amount = get_random_find_amount(material)
            found_materials.append((material, amount))

    return found_materials


def add_found_material_to_inventory(professor, material_name, amount):
    professor.add_material(material_name, amount)


def add_all_found_materials_to_inventory(professor, found_materials):
    for material_name, amount in found_materials:
        professor.add_material(material_name, amount)