from character import Character
from game_time import GameTime
from game_state import GameState


def create_new_game_state(player_name):
    return GameState(
        professor=Character(name=player_name),
        game_time=GameTime(),
    )