from dataclasses import dataclass, field


@dataclass
class Location:
    name: str
    description: str
    smells: list[str] = field(default_factory=list)
    sounds: list[str] = field(default_factory=list)
    visible_materials: list[str] = field(default_factory=list)
    exits: dict[str, str] = field(default_factory=dict)


LOCATIONS = {
    "cave": Location(
        name="Höhle",
        description=(
            "Die Höhle ist dunkel, feucht und still. "
            "Der kalte Steinboden trägt Spuren eines langen Zerfalls."
        ),
        smells=["Salpetersäure"],
        sounds=[],
        visible_materials=[],
        exits={
            "geradeaus": "cave_clearing",
        },
    ),

    "cave_clearing": Location(
        name="Lichtung vor der Höhle",
        description=(
            "Du trittst aus der Höhle heraus und stehst auf einer kleinen Lichtung. "
            "Die Luft ist kühl. Einzelne Spuren der alten Welt sind nicht mehr erkennbar."
        ),
        smells=[],
        sounds=["Waldrauschen", "Vögel"],
        visible_materials=["Stock", "Stein", "Laub"],
        exits={
            "zurück": "cave",
        },
    ),
}