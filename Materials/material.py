from dataclasses import dataclass, field

from Materials.rarity import Rarity


@dataclass
class Material:
    name: str
    rarity: Rarity
    known_by_professor: bool = False
    discovered: bool = False
    properties: list[str] = field(default_factory=list)
    hidden_properties: list[str] = field(default_factory=list)