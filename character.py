from dataclasses import dataclass, field


@dataclass
class Character:
    name: str

    life: int = 100
    max_life: int = 100

    stamina: int = 20
    max_stamina: int = 20

    strength: int = 10
    iq: int = 241
    iq_is_legendary: bool = True

    thirst: int = 20
    hunger: int = 50
    
    inventory: dict[str, list[int]] = field(default_factory=dict)
    discovered_materials: set[str] = field(default_factory=set)

    def life_percent(self):
        return int((self.life / self.max_life) * 100)

    def thirst_percent(self):
        return self.thirst

    def hunger_percent(self):
        return self.hunger

    def strength_stamina_display(self):
        return f"{self.strength}/{self.stamina}"
    
    def add_material(self, material_name, amount=1):
        max_stack_size = 100

        if material_name not in self.inventory:
            self.inventory[material_name] = []

        remaining_amount = amount

        for index in range(len(self.inventory[material_name])):
            free_space = max_stack_size - self.inventory[material_name][index]

            if free_space > 0:
                add_amount = min(remaining_amount, free_space)
                self.inventory[material_name][index] += add_amount
                remaining_amount -= add_amount

            if remaining_amount <= 0:
                break

        while remaining_amount > 0:
            new_stack = min(remaining_amount, max_stack_size)
            self.inventory[material_name].append(new_stack)
            remaining_amount -= new_stack

        self.discovered_materials.add(material_name)
    
    def iq_display(self):
        if self.iq_is_legendary:
            return "Legendär"
        return str(self.iq)
        
    def reset_after_game_over(self):
        self.life = self.max_life
        self.inventory.clear()