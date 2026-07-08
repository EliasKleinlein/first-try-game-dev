from dataclasses import dataclass, field
from enum import Enum
import random


class Rarity(Enum):
    PRIMITIVE = "primitiv"
    COMMON = "gewöhnlich"
    UNCOMMON = "ungewöhnlich"
    RARE = "selten"
    EPIC = "episch"
    LEGENDARY = "legendär"


@dataclass
class Material:
    name: str
    rarity: Rarity
    known_by_professor: bool = False
    discovered: bool = False
    properties: list[str] = field(default_factory=list)
    hidden_properties: list[str] = field(default_factory=list)


STARTING_MATERIALS = [
    Material(
        name="Stock",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=True,
        hidden_properties=["leicht", "brennbar", "bearbeitbar"],
    ),
        Material(
        name="Weichholz",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=True,
        hidden_properties=["weich", "leicht_bearbeitbar", "brennbar"],
    ),
    Material(
        name="Hartholz",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=True,
        hidden_properties=["hart", "stabil", "schwer_bearbeitbar"],
    ),
    Material(
        name="Harter Stein",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=False,
        hidden_properties=["hart", "schlagfest"],
    ),
    Material(
        name="Splitternder Stein",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=False,
        hidden_properties=["spröde", "scharfkantig", "splitternd"],
    ),
    Material(
        name="Weicher Stein",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=False,
        hidden_properties=["weich", "brüchig"],
    ),
    Material(
        name="Laub",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=True,
        hidden_properties=["trockenbar", "brennbar", "isolierend"],
    ),
        Material(
        name="Großes Palmenblatt",
        rarity=Rarity.COMMON,
        known_by_professor=True,
        hidden_properties=["wasserabweisend", "flexibel", "großflächig", "faltbar"],
    ),
    Material(
        name="Bambusreste",
        rarity=Rarity.PRIMITIVE,
        known_by_professor=True,
        hidden_properties=["faserig", "leicht", "flexibel"],
    ),
    Material(
        name="Bambusstange",
        rarity=Rarity.COMMON,
        known_by_professor=True,
        hidden_properties=["hohl", "stabil", "leicht", "flexibel"],
    ),
]
STARTING_FIND_AMOUNTS = {
    "Laub": 10,
    "Großes Palmenblatt": 6,
    "Stock": 8,
    "Stein": 5,
    "Harter Stein": 5,
    "Splitternder Stein": 5,
    "Weicher Stein": 5,
    "Weichholz": 6,
    "Hartholz": 5,
    "Bambusreste": 6,
    "Bambusstange": 3,
}


def get_random_find_amount(material_name):
    base_amount = STARTING_FIND_AMOUNTS.get(material_name, 1)
    variation = random.randint(-2, 2)

    amount = base_amount + variation

    if amount < 1:
        amount = 1

    if amount > 10:
        amount = 10

    return amount