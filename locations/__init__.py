from dataclasses import dataclass, field


@dataclass
class Location:
    name: str
    description: str
    smells: list[str] = field(default_factory=list)
    sounds: list[str] = field(default_factory=list)
    visible_materials: list[str] = field(default_factory=list)
    exits: dict[str, str] = field(default_factory=dict)



from locations.cave import CAVE
from locations.cave_clearing import CAVE_CLEARING
from locations.brook import BROOK
from locations.sea_view import SEA_VIEW
from locations.forest_edge import FOREST_EDGE


LOCATIONS = {
    "cave": CAVE,
    "cave_clearing": CAVE_CLEARING,
    "brook": BROOK,
    "sea_view": SEA_VIEW,
    "forest_edge": FOREST_EDGE,
}