from enum import Enum


class Rarity(Enum):
    PRIMITIVE = "primitiv"
    COMMON = "gewöhnlich"
    UNCOMMON = "ungewöhnlich"
    RARE = "selten"
    EPIC = "episch"
    LEGENDARY = "legendär"


RARITY_FIND_CHANCES = {
    Rarity.PRIMITIVE: 80,
    Rarity.COMMON: 60,
    Rarity.UNCOMMON: 35,
    Rarity.RARE: 15,
    Rarity.EPIC: 7,
    Rarity.LEGENDARY: 3,
}