from locations import Location


SEA_VIEW = Location(
    name="Blick Richtung Meer",
    description=(
        "Der Hang fällt in der Ferne Richtung Meer ab. "
        "Von hier aus ist zu erkennen, dass die Höhle erhöht in einem Berg liegt."
    ),
    smells=["salzige Luft"],
    sounds=["fernes Rauschen"],
    visible_materials=["Stock", "Laub", "Großes Palmenblatt", "Bambusreste"],
    exits={
        "zurück zur Lichtung": "cave_clearing",
    },
)