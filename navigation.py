def get_available_directions(current_location):
    return list(current_location.exits.keys())


def get_location_id_for_direction(current_location, direction_index):
    directions = get_available_directions(current_location)

    if direction_index < 0 or direction_index >= len(directions):
        return None

    selected_direction = directions[direction_index]
    return current_location.exits[selected_direction]