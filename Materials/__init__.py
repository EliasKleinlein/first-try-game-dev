from Materials.rarity import Rarity, RARITY_FIND_CHANCES
from Materials.material import Material
from Materials.starting_materials import STARTING_MATERIALS
from Materials.find_amounts import STARTING_FIND_AMOUNTS
from Materials.material_finding import material_can_be_found, get_random_find_amount
from Materials.material_collection import (
    find_materials_at_location,
    add_found_material_to_inventory,
    add_all_found_materials_to_inventory,
)