from locations import Location


FOREST_EDGE = Location(
    name="Waldrand",
    description=(
        "Vor dir beginnt dichter Wald. "
        "Zwischen den Bäumen liegen vereinzelte Äste, Laub und Spuren von Bambus."
    ),
    smells=["feuchte Erde"],
    sounds=["Vögel", "Waldrauschen"],
    visible_materials=["Stock", "Laub", "Großes Palmenblatt", "Bambusreste"],
    exits={
        "zurück zur Lichtung": "cave_clearing",
    },
)