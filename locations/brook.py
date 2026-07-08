from locations import Location


BROOK = Location(
    name="Bachlauf",
    description=(
        "Ein schmaler Bach fließt zwischen Steinen den Hang hinab. "
        "Das Wasser ist klar, aber noch nicht abgekocht."
    ),
    smells=[],
    sounds=["fließendes Wasser", "Waldrauschen"],
    visible_materials=["Stock", "Laub", "Großes Palmenblatt", "Bambusreste"],
    exits={
        "zurück zur Lichtung": "cave_clearing",
    },
)