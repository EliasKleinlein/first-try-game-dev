from locations import Location


CAVE = Location(
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
)