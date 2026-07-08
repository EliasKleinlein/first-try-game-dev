from locations import Location


CAVE_CLEARING = Location(
    name="Lichtung vor der Höhle",
    description=(
        "Du trittst aus der Höhle heraus und stehst auf einer kleinen Lichtung. "
        "Die Luft ist kühl. Einzelne Spuren der alten Welt sind nicht mehr erkennbar."
    ),
    smells=["Frische Luft"],
    sounds=["Waldrauschen", "Vögel"],
    visible_materials=["Stock", "Laub", "Großes Palmenblatt", "Bambusreste"],
    exits={
        "zurück zur Höhle": "cave",
        "links zum Bach": "brook",
        "rechts Richtung Meer": "sea_view",
        "geradeaus in den Wald": "forest_edge",
    },
)