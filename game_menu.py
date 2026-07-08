from game_setup import create_new_game_state
from game_actions import handle_choice
from terminal_ui import show_intro, show_layout, ask_player_name, ask_menu_choice, wait_for_continue
from night_system import handle_night_if_needed


def main():
    show_intro()

    player_name = ask_player_name()

    state = create_new_game_state(player_name)

    while state.running:
        state.game_time.update()

        handle_night_if_needed(state)

        current_location = state.current_location()
        show_layout(state.professor, state.game_time, current_location)

        choice = ask_menu_choice()

        state.current_location_id = handle_choice(choice, state)

        if state.running:
            wait_for_continue()


main()