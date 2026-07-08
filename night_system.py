import random

from terminal_ui import ask_skip_night, show_night_game_over


def handle_night_if_needed(state):
    if not state.game_time.just_entered_night():
        return

    skip = ask_skip_night()

    if skip.lower() == "j":
        state.game_time.skip_night()
        return

    predator = random.choice(["Löwe", "Tiger", "Wolf", "Bär", "Raubtier"])

    show_night_game_over(predator)

    state.professor.reset_after_game_over()
    state.game_time.skip_night()