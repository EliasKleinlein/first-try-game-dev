def show_inventory(character):
    if not character.inventory:
        print("\nInventar ist leer.")
        return

    print("\nInventar:")

    for material, stacks in character.inventory.items():
        for stack in stacks:
            print(f"- {material}: {stack}x")