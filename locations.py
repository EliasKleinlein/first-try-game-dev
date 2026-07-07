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
            "zurück zur Höhle": "cave",
            "links zum Bach": "brook",
            "rechts Richtung Meer": "sea_view",
            "geradeaus in den Wald": "forest_edge",
        },
    ),
    "brook": Location(
        name="Bachlauf",
        description=(
            "Ein schmaler Bach fließt zwischen Steinen den Hang hinab. "
            "Das Wasser ist klar, aber noch nicht abgekocht."
        ),
        smells=[],
        sounds=["fließendes Wasser", "Waldrauschen"],
        visible_materials=["Stein", "Laub"],
        exits={
            "zurück zur Lichtung": "cave_clearing",
        },
    ),

    "sea_view": Location(
        name="Blick Richtung Meer",
        description=(
            "Der Hang fällt in der Ferne Richtung Meer ab. "
            "Von hier aus ist zu erkennen, dass die Höhle erhöht in einem Berg liegt."
        ),
        smells=["salzige Luft"],
        sounds=["fernes Rauschen"],
        visible_materials=["Stein", "Stock"],
        exits={
            "zurück zur Lichtung": "cave_clearing",
        },
    ),

    "forest_edge": Location(
        name="Waldrand",
        description=(
            "Vor dir beginnt dichter Wald. "
            "Zwischen den Bäumen liegen vereinzelte Äste, Laub und Spuren von Bambus."
        ),
        smells=["feuchte Erde"],
        sounds=["Vögel", "Waldrauschen"],
        visible_materials=["Stock", "Laub", "Bambusreste"],
        exits={
            "zurück zur Lichtung": "cave_clearing",
        },
    ),
}