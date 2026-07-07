from dataclasses import dataclass


@dataclass
class Character:
    name: str

    life: int = 100
    max_life: int = 100

    stamina: int = 20
    max_stamina: int = 20

    strength: int = 10
    iq: int = 241

    thirst: int = 100
    hunger: int = 100

    def life_percent(self):
        return int((self.life / self.max_life) * 100)

    def thirst_percent(self):
        return self.thirst

    def hunger_percent(self):
        return self.hunger

    def strength_stamina_display(self):
        return f"{self.strength}/{self.stamina}"
    
    def iq_display(self):
        if self.name.lower() == "professor":
            return "Legendär"
        return str(self.iq)
        
    def reset_after_game_over(self):
        self.life = self.max_life