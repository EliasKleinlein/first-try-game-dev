from dataclasses import dataclass

from character import Character
from game_time import GameTime
from locations import LOCATIONS


@dataclass
class GameState:
    professor: Character
    game_time: GameTime
    current_location_id: str = "cave"
    running: bool = True

    def current_location(self):
        return LOCATIONS[self.current_location_id]