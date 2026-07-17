import random

from Materials.find_amounts import STARTING_FIND_AMOUNTS
from Materials.rarity import RARITY_FIND_CHANCES
from Materials.starting_materials import STARTING_MATERIALS


def material_can_be_found(material_name):
    for material in STARTING_MATERIALS:
        if material.name == material_name:
            chance = RARITY_FIND_CHANCES[material.rarity]
            roll = random.randint(1, 100)
            return roll <= chance

    return False


def get_random_find_amount(material_name):
    base_amount = STARTING_FIND_AMOUNTS.get(material_name, 1)
    variation = random.randint(-2, 2)

    amount = base_amount + variation

    if amount < 1:
        amount = 1

    if amount > 10:
        amount = 10

    return amount